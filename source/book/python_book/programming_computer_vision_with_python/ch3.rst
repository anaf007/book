第三章：图像到图像的映射
=======================================================================
本章讲解图像之间的变换，以及一些计算变换的实用方法。这些变换可以用于图像 扭曲变形和图像配准。
最后，我们将会介绍一个自动创建全景图像的例子。

3.1　单应性变换
---------------------------------------------------------------------

单应性变换是将一个平面内的点映射到另一个平面内的二维投影变换。在这里，平面是指图像或者三维中的平面表面。
单应性变换具有很强的实用性，比如图像配准、 图像纠正和纹理扭曲，以及创建全景图像。我们将频繁地使用单应性变换。
本质上， 单应性变换 H，按照下面的方程映射二维中的点(齐次坐标意义下):

.. image:: /_static/images/book/1541119944695.jpg
    :width: 400
    :height: 120

对于图像平面内(甚至是三维中的点，后面我们会介绍到)的点，齐次坐 标是个非常有用的表示方式。
点的齐次坐标是依赖于其尺度定义的，所以， x=[x,y,w]=[αx,αy,αw]=[x/w,y/w,1] 都表示同一个二维点。因此，
单应性矩阵 H 也仅 依赖尺度定义，所以，单应性矩阵具有 8 个独立的自由度。我们通常使用 w=1 来归 一化点，这样，
点具有唯一的图像坐标 x 和 y。这个额外的坐标使得我们可以简单 地使用一个矩阵来表示变换。

创建 homography.py 文件。下面的函数可以实现对点进行归一化和转换齐次坐标的功能，将其添加到 homography.py 文件中::

    def normalize(points):
        """ 在齐次坐标意义下，对点集进行归一化，使最后一行为 1 """
        for row in points:
            row /= points[-1]
        return points
    
    def make_homog(points):
        """ 将点集(dim×n 的数组)转换为齐次坐标表示 """

        return vstack((points,ones((1,points.shape[1]))))

进行点和变换的处理时，我们会按照列优先的原则存储这些点。因此，n 个二维点 集将会存储为齐次坐标意义下的一个 3×n 数组。
这种格式使得矩阵乘法和点的变换 操作更加容易。对于其他的例子，比如对于聚类和分类的特征，我们将使用典型的 行数组来存储数据。

在这些投影变换中，有一些特别重要的变换。比如，仿射变换:

.. image:: /_static/images/book/1541121999594.jpg
    :width: 415
    :height: 105


保持了 w=1, 不具有投影变换所具有的强大变形能力。仿射变换包含一个可逆矩阵 A和一个平移向量 t=[tx,ty]。
仿射变换可以用于很多应用，比如图像扭曲。

相似变换:

.. image:: /_static/images/book/1541122132955.jpg
    :width: 536
    :height: 103

是一个包含尺度变化的二维刚体变换。上式中的向量 s 指定了变换的尺度，R 是角 度为 θ 的旋转矩阵，
t=[tx,ty] 在这里也是一个平移向量。如果 s=1，那么该变换能够 保持距离不变。此时，变换为刚体变换。
相似变换可以用于很多应用，比如图像 配准。    

下面让我们一起探讨如何设计用于估计单应性矩阵的算法，然后看一下使用仿射变 换进行图像扭曲，使用相似变换进行图像匹配，
以及使用完全投影变换进行创建全 景图像的一些例子。


3.1.1　直接线性变换算法 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

单应性矩阵可以由两幅图像(或者平面)中对应点对计算出来。前面已经提到过， 一个完全射影变换具有 8 个自由度。
根据对应点约束，每个对应点对可以写出两个 方程，分别对应于 x 和 y 坐标。因此，计算单应性矩阵 H 需要4个对应点对。

DLT(Direct Linear Transformation，直接线性变换)是给定4个或者更多对应点对 矩阵，来计算单应性矩阵 H 的算法。
将单应性矩阵 H 作用在对应点对上，重新写出 该方程，我们可以得到下面的方程:

.. image:: /_static/images/book/1541122425863.jpg
    :width: 490
    :height: 285

或者 Ah=0，其中 A 是一个具有对应点对二倍数量行数的矩阵。将这些对应点对方
程的系数堆叠到一个矩阵中，我们可以使用 SVD(Singular Value Decomposition， 奇异值分解)算法找到 H 的最小二乘解。
下面是该算法的代码。将下面的函数添加 到 homography.py 文件中::

    def H_from_points(fp,tp):
        """ 使用线性 DLT 方法，计算单应性矩阵 H，使 fp 映射到 tp。点自动进行归一化 """
        
        if fp.shape != tp.shape:
            raise RuntimeError('number of points do not match')
        # 对点进行归一化(对数值计算很重要)
        # --- 映射起始点 ---
        m = mean(fp[:2], axis=1)
        maxstd = max(std(fp[:2], axis=1)) + 1e-9 C1 = diag([1/maxstd, 1/maxstd, 1]) C1[0][2] = -m[0]/maxstd
        C1[1][2] = -m[1]/maxstd
        fp = dot(C1,fp)
        
        # --- 映射对应点 ---
        m = mean(tp[:2], axis=1)
        maxstd = max(std(tp[:2], axis=1)) + 1e-9

        C2 = diag([1/maxstd, 1/maxstd, 1])
        C2[0][2] = -m[0]/maxstd
        C2[1][2] = -m[1]/maxstd
        tp = dot(C2,tp)

        # 创建用于线性方法的矩阵，对于每个对应对，在矩阵中会出现两行数值 nbr_correspondences = fp.shape[1]
        A = zeros((2*nbr_correspondences,9))
        for i in range(nbr_correspondences):
            A[2*i] = [-fp[0][i],-fp[1][i],-1,0,0,0,tp[0][i]*fp[0][i],tp[0][i]*fp[1][i],tp[0][i]]
            A[2*i+1] = [0,0,0,-fp[0][i],-fp[1][i],-1,tp[1][i]*fp[0][i],tp[1][i]*fp[1][i],tp[1][i]]
       
        U,S,V = linalg.svd(A)
        H = V[8].reshape((3,3))

        # 反归一化
        H = dot(linalg.inv(C2),dot(H,C1))

        # 归一化，然后返回 
        return H / H[2,2]   

上面函数的第一步操作是检查点对的两个数组中点的数目是否相同。如果不相同， 函数将会抛出异常信息。
这对于写出稳健的代码来说非常有用。但是，为了使得代 码例子更简单、更容易理解，
我们在本书中仅在很少的例子中使用异常处理技巧。 你可以在 http://docs.python.org/library/exceptions.html 
查阅更多关于异常类型的内 容，以及在 http://docs.python.org/tutorial/errors.html 上了解如何使用它们。

对这些点进行归一化操作，使其均值为 0，方差为 1。因为算法的稳定性取决于坐 标的表示情况和部分数值计算的问题，
所以归一化操作非常重要。接下来我们使用 对应点对来构造矩阵 A。最小二乘解即为矩阵 SVD 分解后所得矩阵 V 的最后一行。 
该行经过变形后得到矩阵 H。然后对这个矩阵进行处理和归一化，返回输出。




3.1.2　仿射变换 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

由于仿射变换具有 6 个自由度，因此我们需要三个对应点对来估计矩阵 H。通过将
最后两个元素设置为 0，即 h7=h8=0，仿射变换可以用上面的 DLT 算法估计得出。

这里我们将使用不同的方法来计算单应性矩阵 H，这在文献 [13] 中有详细的描 述(第 130 页)。
下面的函数使用对应点对来计算仿射变换矩阵，将其添加到 homograph.py 文件中::

    def Haffine_from_points(fp,tp):
        """ 计算 H，仿射变换，使得 tp 是 fp 经过仿射变换 H 得到的 """
        if fp.shape != tp.shape:
            raise RuntimeError('number of points do not match')

            # 对点进行归一化
            # --- 映射起始点 ---
            m = mean(fp[:2], axis=1)
            maxstd = max(std(fp[:2], axis=1)) + 1e-9 
            C1 = diag([1/maxstd, 1/maxstd, 1]) 
            C1[0][2] = -m[0]/maxstd

            C1[1][2] = -m[1]/maxstd
            fp_cond = dot(C1,fp)

            # --- 映射对应点 ---
            m = mean(tp[:2], axis=1)
            C2 = C1.copy() # 两个点集，必须都进行相同的缩放 

            C2[0][2] = -m[0]/maxstd
            C2[1][2] = -m[1]/maxstd
            tp_cond = dot(C2,tp)

            # 因为归一化后点的均值为 0，所以平移量为 0
            A = concatenate((fp_cond[:2],tp_cond[:2]), axis=0) 
            U,S,V = linalg.svd(A.T)

            # 如 Hartley 和 Zisserman 著的 Multiple View Geometry in Computer , Scond Edition 所示， 
            # 创建矩阵B和C
            tmp = V[:2].T
            B = tmp[:2]
            C = tmp[2:4]
            tmp2 = concatenate((dot(C,linalg.pinv(B)),zeros((2,1))), axis=1)
            H = vstack((tmp2,[0,0,1]))

            # 反归一化
            H = dot(linalg.inv(C2),dot(H,C1))
            return H / H[2,2]

同样地，类似于 DLT 算法，这些点需要经过预处理和去处理化操作。在下一节中， 让我们一起来看这些仿射变换是如何处理图像的。


3.2　图像扭曲
---------------------------------------------------------------------

对图像块应用仿射变换，我们将其称为图像扭曲(或者仿射扭曲)。该操作不仅经常应用在计算机图形学中，
而且经常出现在计算机视觉算法中。扭曲操作可以使用 SciPy 工具包中的 ndimage 包来简单完成。命令::

    transformed_im = ndimage.affine_transform(im,A,b,size)

使用如上所示的一个线性变换 A 和一个平移向量 b 来对图像块应用仿射变换。选项 参数 size 可以用来指定输出图像的大小。
默认输出图像设置为和原始图像同样大小。为了研究该函数是如何工作的，我们可以试着运行下面的命令::

    from scipy import ndimage
    im = array(Image.open('empire.jpg').convert('L'))
    H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
    im2 = ndimage.affine_transform(im,H[:2,:2],(H[0,2],H[1,2]))

    figure() 
    gray() 
    imshow(im2) 
    show()

该命令输出结果图像如图 3-1(右)所示。可以看到，输出图像结果中丢失的像素用 零来填充。

.. image:: /_static/images/book/1541123400179.jpg
    :width: 420
    :height: 285


3.2.1　图像中的图像 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

仿射扭曲的一个简单例子是，将图像或者图像的一部分放置在另一幅图像中，使得它们能够和指定的区域或者标记物对齐。

将函数 image_in_image() 添加到 warp.py 文件中。该函数的输入参数为两幅图像和 一个坐标。
该坐标为将第一幅图像放置到第二幅图像中的角点坐标::

    def image_in_image(im1,im2,tp):
        """ 使用仿射变换将 im1 放置在 im2 上，使 im1 图像的角和 tp 尽可能的靠近
        tp 是齐次表示的，并且是按照从左上角逆时针计算的 
        """
        # 扭曲的点
        m,n = im1.shape[:2]
        fp = array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])

        # 计算仿射变换，并且将其应用于图像 im1
        H = homography.Haffine_from_points(tp,fp) 
        im1_t = ndimage.affine_transform(im1,H[:2,:2],(H[0,2],H[1,2]),im2.shape[:2])
        alpha = (im1_t > 0)

        return (1-alpha)*im2 + alpha*im1_t

正如你所看到的，该函数没有很多繁杂的操作。将扭曲的图像和第二幅图像融合， 我们就创建了 alpha 图像。
该图像定义了每个像素从各个图像中获取的像素值成分 多少。这里我们基于以下事实，
扭曲的图像是在扭曲区域边界之外以 0 来填充的图 像，来创建一个二值的 alpha 图像。
严格意义上说，我们需要在第一幅图像中的潜 在 0 像素上加上一个小的数值，
或者合理地处理这些 0 像素(参见本章结尾的练习 部分)。注意，这里我们使用的图像坐标是齐次坐标意义下的。

试着使用该函数将公告牌中的一幅图像插入另一幅图像。下面几行代码会将图 3-2 中最左端的图像插入到第二幅图像中。
这些坐标值是通过查看绘制的图像(在 PyLab 图像中，鼠标的坐标显示在图像底部附近)手工确定的。
当然，也可以用 PyLab 类 库中的 ginput() 函数获得。

.. image:: /_static/images/book/1541123726904.jpg
    :width: 430
    :height: 170

::

    import warp
    # 仿射扭曲im1到im2的例子
    im1 = array(Image.open('beatles.jpg').convert('L'))
    im2 = array(Image.open('billboard_for_rent.jpg').convert('L'))

    # 选定一些目标点
    tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])

    im3 = warp.image_in_image(im1,im2,tp)

    figure() 
    gray() 
    imshow(im3) 
    axis('equal') 
    axis('off') 
    show()

上面的代码将图像放置在公告牌的上半部分。需要注意，标记物的坐标 tp 是用齐次 坐标意义下的坐标表示的。将这些坐标换成::

    tp = array([[675,826,826,677],[55,52,281,277],[1,1,1,1]])

会将图像放置在公告牌的左下“for rent”部分。


函数 Haffine_from_points() 会返回给定对应点对的最优仿射变换。在上面的例子 中，对应点对为图像和公告牌的角点。
如果透视效应比较弱，那么这种方法会返回 很好的结果。图 3-3 的上面一行显示出，在具有很强透视效应的情况下，
在公告牌 图像上使用射影变换输出图像的情况。在这种情况下，
我们不可能使用同一个仿射 变换将全部 4 个角点变换到它们的目标位置(尽管我们可以使用完全投影变换来完 成该任务)。
所以，当你打算使用仿射变换时，有一个很有用的技巧。

.. image:: /_static/images/book/1541123924692.jpg
    :width: 850
    :height: 600    

对于三个点，仿射变换可以将一幅图像进行扭曲，使这三对对应点对可以完美地匹配上。
这是因为，仿射变换具有 6 个自由度，三个对应点对可以给出 6 个约束条件 (对于这三个对应点对，x 和 y 坐标必须都要匹配)。
所以，如果你真的打算使用仿 射变换将图像放置到公告牌上，可以将图像分成两个三角形，然后对它们分别进行
扭曲图像操作。下面是具体实现的代码::

    # 选定 im1 角上的一些点
    m,n = im1.shape[:2]
    fp = array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])

    # 第一个三角形 
    tp2 = tp[:,:3] 
    fp2 = fp[:,:3]
    # 计算H
    H = homography.Haffine_from_points(tp2,fp2) 
    im1_t = ndimage.affine_transform(im1,H[:2,:2],(H[0,2],H[1,2]),im2.shape[:2])

    # 三角形的 alpha
    alpha = warp.alpha_for_triangle(tp2,im2.shape[0],im2.shape[1])

    im3 = (1-alpha)*im2 + alpha*im1_t
    # 第二个三角形
    tp2 = tp[:,[0,2,3]] fp2 = fp[:,[0,2,3]]
    
    # 计算H
    H = homography.Haffine_from_points(tp2,fp2) 
    im1_t = ndimage.affine_transform(im1,H[:2,:2],(H[0,2],H[1,2]),im2.shape[:2])
    
    # 三角形的 alpha 图像
    alpha = warp.alpha_for_triangle(tp2,im2.shape[0],im2.shape[1]) 
    im4 = (1-alpha)*im3 + alpha*im1_t

    figure() 
    gray() 
    imshow(im4) 
    axis('equal') 
    axis('off') 
    show()

这里我们简单地为每个三角形创建了 alpha 图像，然后将所有的图像合并起来。
该三 角形的 alpha 图像可以简单地通过检查像素的坐标是否能够写成三角形顶点坐标的凸 组合来计算得出 1。
如果坐标可以表示成这种形式，那么该像素就位于三角形的内部。 
上面的例子使用了下面的函数 alpha_for_triangle()，将其添加到 warp.py 文件中。

::

    def alpha_for_triangle(points,m,n):
        """ 对于带有由 points 定义角点的三角形，创建大小为 (m，n) 的 alpha 图
        (在归一化的齐次坐标意义下)
        """
        alpha = zeros((m,n))
        for i in range(min(points[0]),max(points[0])):
            for j in range(min(points[1]),max(points[1])):
                x = linalg.solve(points,[i,j,1]) 
                if min(x) > 0: # 所有系数都大于零
                    alpha[i,j] = 1
        return alpha

你的显卡可以极其快速地操作上面的代码。Python 语言的处理速度比你的显卡(或 者 C/C++ 实现)慢很多，
但是对于我们来说已经够用了。正如在图 3-3 下半部分所 看到的，角点可以很好地匹配。        


3.2.2　分段仿射扭曲 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

正如上面的例子所示，三角形图像块的仿射扭曲可以完成角点的精确匹配。
让我们 看一下对应点对集合之间最常用的扭曲方式:分段仿射扭曲。给定任意图像的标记 点，通过将这些点进行三角剖分，
然后使用仿射扭曲来扭曲每个三角形，我们可以 将图像和另一幅图像的对应标记点扭曲对应。对于任何图形和图像处理库来说，
这些都是最基本的操作。下面我们来演示一下如何使用Matplotlib 和 SciPy 来完成该 操作。

为了三角化这些点，我们经常使用狄洛克三角剖分方法。
在 Matplotlib(但是不在 PyLab 库中)中有狄洛克三角剖分，我们可以用下面的方式使用它::

    import matplotlib.delaunay as md
    x,y = array(random.standard_normal((2,100)))
    centers,edges,tri,neighbors = md.delaunay(x,y)

    figure()
    for t in tri:
        t_ext = [t[0], t[1], t[2], t[0]] # 将第一个点加入到最后 
        plot(x[t_ext],y[t_ext],'r')

    plot(x,y,'*')
    axis('off')
    show()

图 3-4 显示了一些实例点和三角剖分的结果。狄洛克三角剖分选择一些三角形， 使三角剖分中所有三角形的最小角度最大 1。
函数 delaunay() 有 4 个输出，其中 我们仅需要三角形列表信息(第三个输出)。
在 warp.py 文件中创建用于三角剖分 的函数::

    import matplotlib.delaunay as md 
    def triangulate_points(x,y):
        """ 二维点的 Delaunay 三角剖分 """ 
        centers,edges,tri,neighbors = md.delaunay(x,y)
        return tri

函数输出的是一个数组，该数组的每一行包含对应数组 x 和 y 中每个三角形三个点 的切片。

现在让我们将该算法应用于一个例子，在该例子中，在 5×6 的网格上使用 30 个控 制点，将一幅图像扭曲到另一幅图像中的非平坦区域。
图 3-5b 所示的是将一幅图像 扭曲到“turning torso”的表面。目标点是使用 ginput() 函数手工选取出来的，
将结果保存在 turningtorso_points.txt 文件中。

首先，我们需要写出一个用于分段仿射图像扭曲的通用扭曲函数。下面的代码可以 实现该功能。
在该代码中，我们也展示了如何扭曲一幅彩色图像(你仅需要对每个 颜色通道进行扭曲)。

::

    def pw_affine(fromim,toim,fp,tp,tri): 
        """ 从一幅图像中扭曲矩形图像块
        fromim= 将要扭曲的图像
        toim= 目标图像
        fp= 齐次坐标表示下，扭曲前的点 
        tp= 齐次坐标表示下，扭曲后的点 
        tri= 三角剖分 
        """
        im = toim.copy()

        # 检查图像是灰度图像还是彩色图象 
        is_color = len(fromim.shape) == 3

        # 创建扭曲后的图像(如果需要对彩色图像的每个颜色通道进行迭代操作，那么有必要这样做) 
        im_t = zeros(im.shape, 'uint8')

        for t in tri:
            # 计算仿射变换
            H = homography.Haffine_from_points(tp[:,t],fp[:,t])
            if is_color:
                for col in range(fromim.shape[2]):
                    im_t[:,:,col] = ndimage.affine_transform(fromim[:,:,col],H[:2,:2],\
                        (H[0,2],H[1,2]),im.shape[:2])
            else:
                im_t = ndimage.affine_transform(
                    fromim,H[:2,:2],(H[0,2],H[1,2]),im.shape[:2])

        # 三角形的 alpha
        alpha = alpha_for_triangle(tp[:,t],im.shape[0],im.shape[1])

        # 将三角形加入到图像中 
        im[alpha>0] = im_t[alpha>0]

        return im

在该代码中，我们首先检查该图像是灰度图像还是彩色图像。如果图像为彩色图像， 则对每个颜色通道进行扭曲处理。
因为对于每个三角形来说，仿射变换是唯一确定 的，所以我们这里使用 Haffine_from_points() 函数来处理。
将上面的函数添加到 warp.py 文件中。

为了将该函数应用到当前例子中，接下来的简短脚本将这些操作统一起来::

    import homography
    import warp

    # 打开图像，并将其扭曲
    fromim = array(Image.open('sunset_tree.jpg')) 
    x,y = meshgrid(range(5),range(6))
    x = (fromim.shape[1]/4) * x.flatten()
    y = (fromim.shape[0]/5) * y.flatten()

    # 三角剖分
    tri = warp.triangulate_points(x,y)

    # 打开图像和目标点
    im = array(Image.open('turningtorso1.jpg'))

    tp = loadtxt('turningtorso1_points.txt') # destination points

    # 将点转换成齐次坐标
    fp = vstack((y,x,ones((1,len(x)))))
    tp = vstack((tp[:,1],tp[:,0],ones((1,len(tp)))))

    # 扭曲三角形
    im = warp.pw_affine(fromim,im,fp,tp,tri)

    # 绘制图像
    figure()
    imshow(im) 
    warp.plot_mesh(tp[1],tp[0],tri) 
    axis('off')
    show()

输出结果如图 3-5c 所示。我们通过下面的辅助函数(将其添加到 warp.py 文件中) 来绘制出图像中的这些三角形::

    def plot_mesh(x,y,tri): 
        """ 绘制三角形 """
        for t in tri:
            t_ext = [t[0], t[1], t[2], t[0]] # 将第一个点加入到最后 
            plot(x[t_ext],y[t_ext],'r')

.. image:: /_static/images/book/1541125396988.jpg
    :width: 867
    :height: 415    

这个例子应该能够帮助你在应用中做图像的分段仿射扭曲。我们可以对该例子中的 函数进行改进。
我们将其中一部分留作练习，剩下的留给你自己解决。

3.2.3　图像配准 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

图像配准是对图像进行变换，使变换后的图像能够在常见的坐标系中对齐。
配准可 以是严格配准，也可以是非严格配准。为了能够进行图像对比和更精细的图像分析，
图像配准是一步非常重要的操作。

让我们一起看一个对多个人脸图像进行严格配准的例子。该配准使得我们计算的平均人脸和人脸表观的变化具有意义。
因为，图像中的人脸并不都有相同的大小、位 置和方向，所以，在这种类型的配准中，
我们实际上是寻找一个相似变换(带有尺 度变化的刚体变换)，在对应点对之间建立映射。

在 jkface.zip 文件中有 366 幅单人图像(2008 年，每天一幅)。1 这些图像都对眼睛 和嘴的坐标进行了标记，
结果保存在 jkface.xml 文件中。使用这些点，我们可以计 算出一个相似变换，
然后将可以使用该变换(包含尺度变换)的这些图像扭曲到一 个归一化的坐标系中。为了读取 XML 格式的文件，
我们将会使用 Python 中内置 xml.dom 模块中的 minidom 类库。

该 XML 文件看起来类似于下面的格式::

    <?xml version="1.0" encoding="utf-8"?>
    <faces>
    <face file="jk-002.jpg" xf="46" <face file="jk-006.jpg" xf="38" <face file="jk-004.jpg" xf="40" <face file="jk-010.jpg" xf="33"
    xm="56" xs="67" yf="38" ym="65" ys="39"/>
    xm="48" xs="59" yf="38" ym="65" ys="38"/>
    xm="50" xs="61" yf="38" ym="66" ys="39"/>
    xm="44" xs="55" yf="38" ym="65" ys="38"/>
    ...
    </faces>

为了从该文件中读取这些坐标，我们需要将使用 minidom 的函数添加到新文件imregistration.py 中::

    from xml.dom import minidom
    def read_points_from_xml(xmlFileName): 
        """ 读取用于人脸对齐的控制点 """

        xmldoc = minidom.parse(xmlFileName)
        facelist = xmldoc.getElementsByTagName('face')
        faces = {}

        for xmlFace in facelist:
            fileName = xmlFace.attributes['file'].value 
            xf = int(xmlFace.attributes['xf'].value)
            yf = int(xmlFace.attributes['yf'].value)
            xs = int(xmlFace.attributes['xs'].value)
            ys = int(xmlFace.attributes['ys'].value)
            xm = int(xmlFace.attributes['xm'].value)
            ym = int(xmlFace.attributes['ym'].value) 
            faces[fileName] = array([xf, yf, xs, ys, xm, ym])
        return faces

这些标记点会在 Python 中以字典的形式返回，字典的键值为图像的文件名。
格式 为:图像中左眼(人脸右侧)的坐标为 xf 和 yf，右眼的坐标为 xs 和 ys，嘴的坐标 为 xm 和 ym。
为了计算相似变换中的参数，我们可以使用最小二乘解来解决。对于 每个点 xi=[xi, yi](在这个例子中，每幅图像有三个点)，
这些点应该被映射到目标位tt置[xi, yi]，如下所示:

.. image:: /_static/images/book/1541125671577.jpg
    :width: 235
    :height: 80       

将这三个点都表示成该形式，我们可以重新将其写成方程组的形式。该方程组中含有 a、b、tx、ty 未知量，如下所示:       

.. image:: /_static/images/book/1541125717262.jpg
    :width: 235
    :height: 200      

下面我们使用相似矩阵的参数化表示方式:

.. image:: /_static/images/book/1541125761369.jpg
    :width: 600
    :height: 145      

如果存在更多的对应点对，其计算公式相同，只需在矩阵中额外添加几行。
你可以 使用 linalg.lstsq() 函数来计算该问题的最小二乘解。 使用最小二乘解的思想是一 个标准技巧，
我们还会在本书中多次使用。实际上，这和之前在 DLT 算法中使用的 方式相同。

函数的具体代码如下(将其添加到 imregistration.py 文件中)::

    from scipy import linalg
    def compute_rigid_transform(refpoints,points):
        """ 计算用于将点对齐到参考点的旋转、尺度和平移量 """
        A = array([ [points[0], -points[1], 1, 0],
                    [points[1],  points[0], 0, 1],
                    [points[2], -points[3], 1, 0],
                    [points[3],  points[2], 0, 1],
                    [points[4], -points[5], 1, 0],
                    [points[5],  points[4], 0, 1]])

        y = array([ refpoints[0], 
                    refpoints[1], 
                    refpoints[2], 
                    refpoints[3], 
                    refpoints[4],
                    refpoints[5]])

        # 计算最小化 ||Ax-y|| 的最小二乘解
        a,b,tx,ty = linalg.lstsq(A,y)[0]
        R = array([[a, -b], [b, a]]) # 包含尺度的旋转矩阵
        
        return R,tx,ty

该函数返回一个具有尺度的旋转矩阵，以及在 x 和 y 方向上的平移量。为了扭曲图 像，并保存对齐后的新图像，
我们可以对每个颜色通道(这些图像都是彩色图像) 应用 ndimage.affine_transform() 函数操作。作为参考坐标系，
你可以使用任何三 个点的坐标。这里我们为了简单起见，直接使用第一幅图像中的标记位置::

    from scipy import ndimage 
    from scipy.misc import imsave 
    import os

    def rigid_alignment(faces,path,plotflag=False): 
        """ 严格对齐图像，并将其保存为新的图像
            path 决定对齐后图像保存的位置
            设置 plotflag=True，以绘制图像 
        """
        # 将第一幅图像中的点作为参考点 refpoints = faces.values()[0]
        # 使用仿射变换扭曲每幅图像 
        for face in faces:
            points = faces[face]
        R,tx,ty = compute_rigid_transform(refpoints, points) 
        T = array([[R[1][1], R[1][0]], [R[0][1], R[0][0]]])

        im = array(Image.open(os.path.join(path,face))) 
        im2 = zeros(im.shape, 'uint8')

        # 对每个颜色通道进行扭曲
        for i in range(len(im.shape)):
            im2[:,:,i] = ndimage.affine_transform(im[:,:,i],linalg.inv(T),offset=[-ty,-tx])

        if plotflag: 
            imshow(im2) 
            show()
        # 裁剪边界，并保存对齐后的图像 
        h,w = im2.shape[:2]
        border = (w+h)/20

        # 裁剪边界
        imsave(os.path.join(path, 'aligned/'+face),im2[border:h-border,border:w-border,:])

这里我们使用 imsave() 函数来将对齐后的图像保存到 aligned 子文件夹中。

接下来的简短脚本会读取 XML 文件，其中文件名为键，点的坐标为键值。然后配准所有的图像，将它们与第一幅图像对齐::

    import imregistration

    # 载入控制点的位置
    xmlFileName = 'jkfaces2008_small/jkfaces.xml'
    points = imregistration.read_points_from_xml(xmlFileName)

    # 注册 
    imregistration.rigid_alignment(points,'jkfaces2008_small/')

运行这些代码，你能够在子目录中得到这些对齐后的人脸图像。图 3-6 所示为配准 前后的 6 幅样本图像。
由于配准后图像的边界可能会出现不想要的黑色填充像素， 所以我们对配准后的图像进行轻微的修剪，来删除这些黑色填充像素。    

.. image:: /_static/images/book/1541126160462.jpg
    :width: 834
    :height: 388      

现在让我们看配准操作如何影响平均图像。图 3-7 为未对齐人脸图像的平均图像， 旁边是对齐后图像的平均图像。
(注意，由于对齐后图像的边界有裁剪，所以两幅图 像的大小有差异)尽管在原始图像中，人脸的尺寸、方向和位置变化都很小，
但是 配准操作对平均图像的计算结果影响很大。

自然地，使用未准确配准的图像同样对主成分的计算结果有着很大的影响。图 3-8 表示，
从未经过配准和经过配准的数据集中选取前 150 幅图像，PCA 的计算结果。 正如平均图像一样，未配准的 PCA 模式是模糊的。
在计算主成分时，我们使用以平 均人脸位置为中心的椭圆掩膜。在堆叠这些图像之前，将这些图像和掩膜相乘，
我 们能够避免将背景变化带入到 PCA 模式中。将 1.3 节 PCA 例子中创建矩阵的一行 替换为::

    immatrix = array([mask*array(Image.open(imlist[i]).convert('L')).flatten() for i in range(150)],'f')

其中 mask 是一副同样大小的二值图像，已经经过压平处理。


3.3　创建全景图
---------------------------------------------------------------------

在同一位置(即图像的照相机位置相同)拍摄的两幅或者多幅图像是单应性相关的 (如图 3-9 所示)。
我们经常使用该约束将很多图像缝补起来，拼成一个大的图像来创建全景图像。在本节中，我们将探讨如何创建全景图像。

.. image:: /_static/images/book/1541126364831.jpg
    :width: 831
    :height: 456      



3.3.1 RANSAC 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

RANSAC 是“RANdom SAmple Consensus”(随机一致性采样)的缩写。该方法是 用来找到正确模型来拟合带有噪声数据的迭代方法。
给定一个模型，例如点集之间 的单应性矩阵，RANSAC 基本的思想是，数据中包含正确的点和噪声点，
合理的模 型应该能够在描述正确数据点的同时摒弃噪声点。

RANSAC 的标准例子:用一条直线拟合带有噪声数据的点集。简单的最小二乘在该 例子中可能会失效，
但是 RANSAC 能够挑选出正确的点，然后获取能够正确拟合 的直线。下面来看使用 RANSAC 的例子。
你可以从 http://www.scipy.org/Cookbook/ RANSAC 下载 ransac.py，里面包含了特定的例子作为测试用例。
图 3-10 为运行 ransac.text() 的例子。可以看到，该算法只选择了和直线模型一致的数据点，成功 地找到了正确的解。

RANSAC 是个非常有用的算法，我们将在下一节估计单应性矩阵和其他一些例子中 使用它。
关于 RANSAC 更多的信息，参见 Fischler 和 Bolles 的原始论文 [11]、
维基 百科 http://en.wikipedia.org/wiki/RANSAC 或者技术报告 [40]。


3.3.2　稳健的单应性矩阵估计 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

我们在任何模型中都可以使用 RANSAC 模块。在使用 RANSAC 模块时，
我们只需 要在相应 Python 类中实现 fit() 和 get_error() 方法，剩下就是正确地使用 ransac.py。 
我们这里使用可能的对应点集来自动找到用于全景图像的单应性矩阵。图 3-11 所示 为使用 SIFT 特征自动找到匹配对应。
这可以通过运行下面的命令来实现::

    import sift
    featname = ['Univ'+str(i+1)+'.sift' for i in range(5)]
    imname = ['Univ'+str(i+1)+'.jpg' for i in range(5)]
    l = {}
    d = {}

    for i in range(5): 
        sift.process_image(imname[i],featname[i])
        l[i],d[i] = sift.read_features_from_file(featname[i])
    
    matches = {}
    for i in range(4):
        matches[i] = sift.match(d[i+1],d[i])

显然，并不是所有图像中的对应点对都是正确的。实际上，SIFT 是具有很强稳健性 的描述子，能够比其他描述子，
例如图像块相关的 Harris 角点，产生更少的错误的 匹配。但是该方法仍然远非完美。        

.. image:: /_static/images/book/1541126589118.jpg
    :width: 858
    :height: 638      

我们使用 RANSAC 算法来求解单应性矩阵，首先需要将下面模型类添加到homography.py 文件中::

    class RansacModel(object):
        """ 用于测试单应性矩阵的类，其中单应性矩阵是由网站 http://www.scipy.org/Cookbook/RANSAC 上
        的 ransac.py 计算出来的 
        """

        def __init__(self,debug=False):
            self.debug = debug def fit(self, data):

            """ 计算选取的 4 个对应的单应性矩阵 """
            # 将其转置，来调用 H_from_points() 计算单应性矩阵
            data = data.T
            # 映射的起始点 
            fp = data[:3,:4] 
            # 映射的目标点 
            tp = data[3:,:4]
            # 计算单应性矩阵，然后返回 
            return H_from_points(fp,tp)

        def get_error( self, data, H):
            """ 对所有的对应计算单应性矩阵，然后对每个变换后的点，返回相应的误差 """
            data = data.T
            # 映射的起始点 
            fp = data[:3] 
            # 映射的目标点 
            tp = data[3:]
            # 变换fp

            fp_transformed = dot(H,fp)
            # 归一化齐次坐标 
            for i in range(3):
                fp_transformed[i] /= fp_transformed[2]

            # 返回每个点的误差
            return sqrt( sum((tp-fp_transformed)**2,axis=0) )

可以看到，这个类包含 fit() 方法。该方法仅仅接受由 ransac.py 选择的4个对应点 对(data 中的前4个点对)，
然后拟合一个单应性矩阵。记住，4个点对是计算单 应性矩阵所需的最少数目。
由于 get_error() 方法对每个对应点对使用该单应性矩 阵，然后返回相应的平方距离之和，
因此 RANSAC 算法能够判定哪些点对是正确 的，哪些是错误的。在实际中，
我们需要在距离上使用一个阈值来决定哪些单应性 矩阵是合理的。为了方便使用，
将下面的函数添加到 homography.py 文件中::

    def H_from_ransac(fp,tp,model,maxiter=1000,match_theshold=10): 
        """ 使用 RANSAC 稳健性估计点对应间的单应性矩阵 H(ransac.py 为从
            http://www.scipy.org/Cookbook/RANSAC 下载的版本)
            # 输入:齐次坐标表示的点 fp，tp(3×n 的数组)""" 

            import ransac

            # 对应点组
            data = vstack((fp,tp))
            # 计算 H，并返回
            H,ransac_data = ransac.ransac(data.T,model,4,maxiter,match_theshold,10,
                    return_all=True)

            return H,ransac_data['inliers']

该函数同样允许提供阈值和最小期望的点对数目。最重要的参数是最大迭代次数: 程序退出太早可能得到一个坏解;
迭代次数太多会占用太多时间。函数的返回结果 为单应性矩阵和对应该单应性矩阵的正确点对。   

类似于下面的操作，你可以将 RANSAC 算法应用于对应点对上::

    # 将匹配转换成齐次坐标点的函数 
    def convert_points(j):
        ndx = matches[j].nonzero()[0]
        fp = homography.make_homog(l[j+1][ndx,:2].T) 
        ndx2 = [int(matches[j][i]) for i in ndx]
        tp = homography.make_homog(l[j][ndx2,:2].T) 
        return fp,tp

    # 估计单应性矩阵
    model = homography.RansacModel()

    fp,tp = convert_points(1)
    H_12 = homography.H_from_ransac(fp,tp,model)[0] # im1 到 im2 的单应性矩阵

    fp,tp = convert_points(0)
    H_01 = homography.H_from_ransac(fp,tp,model)[0] # im0 到 im1 的单应性矩阵

    tp,fp = convert_points(2) # 注意:点是反序的
    H_32 = homography.H_from_ransac(fp,tp,model)[0] # im3 到 im2 的单应性矩阵

    tp,fp = convert_points(3) # 注意:点是反序的
    H_43 = homography.H_from_ransac(fp,tp,model)[0] # im4 到 im3 的单应性矩阵         

在该例子中，图像 2 是中心图像，也是我们希望将其他图像变成的图像。图像 0 和 图像 1 应该从右边扭曲，
图像 3 和图像 4 从左边扭曲。在每个图像对中，由于匹配 是从最右边的图像计算出来的，所以我们将对应的顺序进行了颠倒，
使其从左边图 像开始扭曲。因为我们不关心该扭曲例子中的正确点对，所以仅需要该函数的第一 个输出(单应性矩阵)。



3.3.3　拼接图像 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

估计出图像间的单应性矩阵(使用 RANSAC 算法)，现在我们需要将所有的图像扭 曲到一个公共的图像平面上。
通常，这里的公共平面为中心图像平面(否则，需要 进行大量变形)。一种方法是创建一个很大的图像，比如图像中全部填充 0，
使其和 中心图像平行，然后将所有的图像扭曲到上面。由于我们所有的图像是由照相机水平 旋转拍摄的，
因此我们可以使用一个较简单的步骤:将中心图像左边或者右边的区域填充0，以便为扭曲的图像腾出空间。
将下面的代码添加到 warp.py 文件中::

    def panorama(H,fromim,toim,padding=2400,delta=2400):
        """ 使用单应性矩阵 H(使用 RANSAC 健壮性估计得出)，协调两幅图像，创建水平全景图像。结果
            为一幅和 toim 具有相同高度的图像。padding 指定填充像素的数目，delta 指定额外的平移量 
        """ 

        # 检查图像是灰度图像，还是彩色图像

        is_color = len(fromim.shape) == 3
        # 用于 geometric_transform() 的单应性变换 

        def transf(p):
            p2 = dot(H,[p[0],p[1],1])
            return (p2[0]/p2[2],p2[1]/p2[2])

        if H[1,2]<0: # fromim 在右边 
            print 'warp - right'
            # 变换 fromim
            if is_color:
                # 在目标图像的右边填充 0
                toim_t = hstack((toim,zeros((toim.shape[0],padding,3))))
                fromim_t = zeros((toim.shape[0],toim.shape[1]+padding,toim.shape[2])) 
                for col in range(3):
                    fromim_t[:,:,col] = ndimage.geometric_transform(fromim[:,:,col],
                        transf,(toim.shape[0],toim.shape[1]+padding))

            else:
                # 在目标图像的右边填充 0
                toim_t = hstack((toim,zeros((toim.shape[0],padding)))) 
                fromim_t = ndimage.geometric_transform(fromim,transf,
                            (toim.shape[0],toim.shape[1]+padding))

        else:
            print 'warp - left'
            # 为了补偿填充效果，在左边加入平移量
            H_delta = array([[1,0,0],[0,1,-delta],[0,0,1]])
            H = dot(H,H_delta)
            # fromim 变换
            if is_color:
                # 在目标图像的左边填充 0
                toim_t = hstack((zeros((toim.shape[0],padding,3)),toim))
                fromim_t = zeros((toim.shape[0],toim.shape[1]+padding,toim.shape[2])) 
                for col in range(3):
                    fromim_t[:,:,col] = ndimage.geometric_transform(fromim[:,:,col],
                        transf,(toim.shape[0],toim.shape[1]+padding))

            else:
                # 在目标图像的左边填充 0
                toim_t = hstack((zeros((toim.shape[0],padding)),toim)) 
                fromim_t = ndimage.geometric_transform(fromim,
                    transf,(toim.shape[0],toim.shape[1]+padding))

                # 协调后返回(将 fromim 放置在 toim 上) 
                if is_color:
                    # 所有非黑色像素
                    alpha = ((fromim_t[:,:,0] * fromim_t[:,:,1] * fromim_t[:,:,2] ) > 0) 
                    for col in range(3):
                        toim_t[:,:,col] = fromim_t[:,:,col]*alpha + toim_t[:,:,col]*(1-alpha)

                else:
                    alpha = (fromim_t > 0)
                    toim_t = fromim_t*alpha + toim_t*(1-alpha)

        return toim_t

**书中 代码对齐补全，缩进可能会有问题**

对于通用的 geometric_transform() 函数，我们需要指定能够描述像素到像素间映射 的函数。
在这个例子中，transf() 函数就是该指定的函数。该函数通过将像素和 H 相乘，然后对齐次坐标进行归一化来实现像素间的映射。
通过查看 H 中的平移量， 我们可以决定应该将该图像填补到左边还是右边。当该图像填补到左边时，
由于目 标图像中点的坐标也变化了，所以在“左边”情况中，需要在单应性矩阵中加入平 移。简单起见，
我们同样使用 0 像素的技巧来寻找 alpha 图。 

现在在图像中使用该操作，函数如下所示::

    # 扭曲图像
    delta = 2000 # 用于填充和平移
    im1 = array(Image.open(imname[1]))
    im2 = array(Image.open(imname[2]))
    im_12 = warp.panorama(H_12,im1,im2,delta,delta)

    im1 = array(Image.open(imname[0]))
    im_02 = warp.panorama(dot(H_12,H_01),im1,im_12,delta,delta)

    im1 = array(Image.open(imname[3]))
    im_32 = warp.panorama(H_32,im1,im_02,delta,delta)

    im1 = array(Image.open(imname[j+1]))
    im_42 = warp.panorama(dot(H_32,H_43),im1,im_32,delta,2*delta)

注意，在最后一行中，im_32 图像已经发生了一次平移。创建的全景图结果如 图 3-12 所示。
正如你所看到的，图像曝光不同，在单个图像的边界上存在边缘效 应。
商业的创建全景图像软件里有额外的操作来对强度进行归一化，并对平移进行 平滑场景转换，以使得结果看上去更好。

.. image:: /_static/images/book/1541127332817.jpg
    :width: 836
    :height: 411  

练习
---------------------------------------------------------------------

1.写出一个函数，其输入参数为正方形(或者长方形)物体(例如，一本书、一张 海报，或者二维条形码)图像的坐标。
然后，计算将该长方形映射归一化坐标系 中正视图全图的变换。你可以使用 ginput()，
或者最强的 Harris 角点来发现长方 形物体的稳健性角点。

2.写出一个函数，对于如图 3-1 所示的扭曲能够正确地找到 alpha 图像。

3.在你自己的数据集中找出包含三个公共的标记物(像人脸例子一样，或者使用著 名的景物，比如埃菲尔铁塔)的那个。
创建对齐后的图像，其中这些标记物在同一个位置上。计算平均和中值图像，然后可视化。

4.进行亮度归一化操作，找出在全景图像例子中更好地拼接图像的方法。该方法能够去除图 3-12 中的边缘效应。

5.与将图像扭曲到中心图像上不同，全景图像可以通过将图像扭曲到圆柱体上来创建。

6.使用 RANSAC 算法来找到一些主要的正确单应性矩阵集合。一个简单的方式是，首先运行一次 RANSAC 算法，
找到具有最大一致子集的单应性矩阵，然后 将与该单应性矩阵一致的对应点对从匹配集合中删除，
再运行 RANSAC 算法找 到下一个最大的集合，以此类推。

7.修改单应性矩阵的 RANSAC 估计算法，来使用三个对应点对计算仿射变换。
使 用该算法来判断图像对之间是否包含平面场景，例如使用正确点的个数。
对于仿 射变化，平面场景中正确点的个数会很多。

8.通过匹配局部特征，以及使用最小二乘刚体配准，
用多个图像(例如，从 Flickr 下载)创建一个全景图(http://en.wikipedia.org/wiki/Panography)。






