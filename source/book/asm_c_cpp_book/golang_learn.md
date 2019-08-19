GoLang的学习
==================================================================

原链接： https://www.jianshu.com/nb/30833789

1、环境搭建和运行
---------------------------------------------------------------

下载go程序并安装

输入 ``go version`` 出现版本号说明正常

第一个go程序


```
package main
import "fmt"
func main(){
	fmt.Print("hello golang")
}
```

``必须有一个main包  一个main函数  花括号必须在同行``

运行： ``go run index.go``

或者编译exe： ``go build index.go``


2、 基础语法
---------------------------------------------------------------

四种方式：
 * 完全体：var name type
 * 类型推断：var name = value
 * 最简体：name := value（仅用于函数内变量，包内变量不行）
 * 变量聚合定义：var( name1=value1 name2=value2 )

```
package main

import "fmt"

// 定义包内变量
var (
    aa = 1
    bb = "tianya"
)

// 定义变量，只使用默认初值
func variableZeroValue()  {
    var a int       // 0
    var s string    // ""
    var b bool      // false
    fmt.Println(a, s, b)
}

// 定义变量，赋初值
func variableInitialValue()  {
    var a, b int = 1, 2
    b = 3
    var s string = "haha"
    fmt.Println(a, b, s)
}

// 类型推断
func variableTypeDeduction()  {
    var a, b, c, d  = 1, 2, true, "hi"
    fmt.Println(a, b, c, d)
}

// 最简定义变量方式
func variableShorter() {
    a, b, c, d := 3, 2, true, "hi"
    fmt.Println(a, b, c, d)
}

func main() {
    variableZeroValue()
    variableInitialValue()
    variableTypeDeduction()
    variableShorter()
    fmt.Println(aa, bb)
}

// 强制类型转换
func triangle()  {
    var a, b int = 3, 4
    var c int
    // float64 和 int 可以不加小括号，也可以加上
    // 开方内建函数定义：func Sqrt(x float64) float64
    c = int(math.Sqrt(float64(a*a + b*b)))
    fmt.Println(c)
}

//常量与枚举
const name type = value
const name = value

自定义枚举：const ( name1=value1 name2=value2 )
iota 表达式枚举：const ( name1=iota表达式 name2 )

// 常量
func consts() {
    // 指定类型
    const filename string = "filename-const"
    // 不指定类型，表示类型不定
    const a, b = 3, 4
    var c int
    // 由于类型不定，所以这里不需要强转，如果定义为 const a, b int = 3, 4，则需要强转
    c = int(math.Sqrt(a*a + b*b))
    fmt.Println(filename, a, b, c)
}

// 枚举
func enums() {
    // 使用 const 块来实现枚举
    const (
        java = 0
        cpp  = 1
        c    = 2
    )
    fmt.Println(java, cpp, c) // 0 1 2
    // 使用 iota 块来实现自增枚举
    const (
        java1 = iota
        cpp1  
        c1    
    )
    fmt.Println(java1, cpp1, c1) // 0 1 2
}


//条件语句
~=!注意：if：变量可以定义在 if 块内，其作用域就只在 if 块内了
import (
    "io/ioutil"
    "fmt"
)

func readFile() {
    const filename = "abc.txt"
    // Go 函数可以返回两个值
    // func ReadFile(filename string) ([]byte, error)
    contents, err := ioutil.ReadFile(filename)
    if err != nil {
        fmt.Println(err)
    } else {
        // contents 是 []byte, 用%s 可以打印出来
        fmt.Printf("%s", contents)
    }
    // if 语句外部可访问
    fmt.Printf("%s", contents)
}

func readFileShorter() {
    const filename = "abc.txt"
    // Go 函数可以返回两个值
    // func ReadFile(filename string) ([]byte, error)

    if contents, err := ioutil.ReadFile(filename); err != nil {
        fmt.Println(err)
    } else {
        // contents 是 []byte, 用%s 可以打印出来
        fmt.Printf("%s", contents)
    }
    // if 语句外部不可访问
    //fmt.Printf("%s", contents) // 报错
}

// switch 默认自带break，如果想穿下去执行，使用 fallthrough
func eval(a, b int, op string) int  {
    var value int
    switch op {
    case "+":
        value = a + b
    case "-":
        value = a - b
    default:
        panic("unsupport operator" + op)
    }
    return value
}

//for：for 的三个组件都可省略，Go 没有 while，用 for 来替代

import (
    "fmt"
    "os"
    "bufio"
)

func sum() int {
    var value int
    for i := 0; i <= 100; i++ {
        value += i
    }
    return value
}

// 等同于 while(true)
func deadLoop() {
    for {
        fmt.Println("this is a deadLoop")
    }
}

// Go 没有while，循环全部用 for，for的三个组件都可以省略
func printFile(filename string) {
    // 打开文件
    file, err := os.Open(filename)
    // 如果出错，结束进程
    if err != nil {
        panic(err)
    }
    // 获取读取器
    scanner := bufio.NewScanner(file)
    // 读取：It returns false when the scan stops, either by reaching the end of the input or an error
    for scanner.Scan() {
        fmt.Println(scanner.Text())
    }
}

################函数$#$$$$$$$$#$@@@@@@@@@@@@
func 函数
	可以有多个返回值
	函数的参数类型可以是 func - 函数式编程
	支持可变长参数

======================== 可以有多个返回值 =========================
// 函数可返回多个值
// 接收：q, r := div(10, 3)
// 如果只用其中一个值，另一个用下划线：q, _ := div(10, 3)
func div(a, b int) (int, int) {
    return a / b, a % b
}
// use
q, _ := div(10, 3)

======================== 函数的参数类型可以是 func =========================
// 可以使用函数作为参数，函数参数与内部参数一样，函数名在前，函数类型在后
// 后续传参，可以使用匿名内部函数，也可以先定义函数再传入
func apply(op func(int, int) int, a,b int) int {
    return op(a, b)
}
// use
result := apply(func(x int, y int) int {
    return x + y
}, 10,4)

======================== 支持可变长参数 =========================
// 可变长参数
func sum2(nums ...int) int {
    s := 0
    for i := range nums {
        s += nums[i]
    }
    return s
}
// use
sum2(1, 2, 3)


@@@@@@@@@@@指针####################
Go 只有值传递，引用传递需要借助指针实现
引用传递实际上也是值传递，只是传递的是地址

// 值传递，函数参数拷贝了一份外界的 a, b
func swap_by_value(a, b int) {
    b, a = a, b
}
// use
a, b := 3, 4
swap_by_value(a, b)
fmt.Println(*(&a), b) // 3 4 没有实现交换

函数参数拷贝了一份外界的 a, b

// Go 只有值传递，想实现引用传递，使用指针
// *int 代表是指针类型，此时会将外界传入的 &a 拷贝给 这里的a，即这里的 a 拿到的是外界的 a 的地址
// 通过 *a，由于 a 是 &a，这里的 *a 相当于 *(&a) ，即从地址中取值
// 由于函数内部直接操作的是外界的 a,b 的内存地址，所以可以实现引用传递
func swap_by_pointer(a, b *int) {
    *b, *a = *a, *b
}
// use
swap_by_pointer(&a, &b)
fmt.Println(a, b)

*int 代表是指针类型，此时会将外界传入的 &a 拷贝给 这里的a，即这里的 a 拿到的是外界的 a 的地址
通过 *a，由于 a 是 &a，这里的 *a 相当于 *(&a) ，即从地址中取值
由于函数内部直接操作的是外界的 a,b 的内存地址，所以可以实现引用传递
```


3、 内建容易——array数组、slice切片、map映射
---------------------------------------------------------------

[原文链接](https://www.jianshu.com/p/78975d33a018)  和Python不一样的  一时还是无法理解 有些晦涩难懂


4、面向对象
---------------------------------------------------------------


1、 定义类

定义类：type 类名 struct

```
// user 类
type user struct {
    name       string
    email      string
    ext        int
    privileged bool
}

// admin 类
type admin struct {
    // 自定义类
    person user
    // 内置类型
    level string
}


```

1.2、 实例化

```
// 1. 创建 user 变量，所有属性初始化为其零值
    var bill user
    fmt.Println(bill) // {  0 false}

    // 2. 创建 user 变量，并初始化属性值
    lisa := user{
        name:       "nana",
        email:      "117@qq.com",
        ext:        123,
        privileged: true,
    }
    fmt.Println(lisa) // {nana 117@qq.com 123 true}
    // 直接使用属性值，属性值的顺序要与 struct 中定义的一致
    lisa2 := user{"nana", "117@qq.com", 123, true}
    fmt.Println(lisa2) // {nana 117@qq.com 123 true}

    // 3. 含有自定义类型的 struct 进行初始化
    fred := admin{
        person: user{
            name:       "nana",
            email:      "117@qq.com",
            ext:        123,
            privileged: true,
        },
        level: "super",
    }
    fmt.Println("fred:", fred) // fred: {{nana 117@qq.com 123 true} super}
```



