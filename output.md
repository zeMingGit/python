## 1.认识 flex 布局

我们在写前端页面的时候可能会遇到这样的问题：同样的一个页面在 1920x1080 的大屏幕中显示正常，但是在 1366x768 的小屏幕中却显示的非常凌乱。

这是因为我们开发的页面不能做到**自适应屏幕大小** 。为了解决这个问题，弹性布局应运而生。

> flex 布局又叫做弹性布局，它是一种页面元素的布局方式。说白了就是按照这种布局方式，页面的元素可以**自适应**
> 屏幕尺寸的大小。不管屏幕尺寸是大还是小，页面的元素依然排列的很整齐，看起来不会那么凌乱。

我们开发的前端页面中有 div、p、ul 等各种元素标签，那如何才能让这些元素处于弹性布局中呢？

所以 flex 布局的核心是要先有一个"弹性容器"，容器中的所有元素都处在弹性布局中。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/OMQfyHAM9YqqIANFXKSQYZRR8tWWwOUXgycYATVZOoRgMKuAwJGz20tg1LwQFS4wtjC7oJD6MB7mjOTQjcWNYg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

任何一个元素标签都可以作为弹性布局容器，比如 div、span、p 标签等。

只要设置下面的 css 属性，这些标签就变成了一个弹性容器：

```
 /* 表示该元素是弹性容器 */  
 display: flex;  

```

有了弹性容器之后，我们需要为该容器和它的子元素设置相关的属性，这样才能达到我们想要的弹性布局效果。

## 2\. 容器属性

### 2.1 flex-direction

> flex-direction ：字面意思是**弹性布局的方向** ，说白了就是这个**弹性容器中的元素** 以什么方向排列。默认是横向排列。

我们把元素的排列方向叫做主轴，与之对应的叫做侧轴。如果属性值是 row ,那主轴就是 X 轴，侧轴就是 Y 轴。如果属性值是 column ,那主轴就是 Y
轴，侧轴就是 X 轴。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**属性值：**

  * row：横向排列，从左到右
  * row-reverse：横向排列，从右到左
  * column：竖向排列，从上到下
  * column-reverse：竖向排列，从下到上

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 2.2 justify-content

> justify-content ：子元素的排列方式，默认是 flex-start。

属性值：

  * flex-start
  * flex-end
  * center
  * space-around
  * space-between

因为 flex-direction 默认值是 row，所以子元素默认横向排列。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

如果容器设置 flex-direction: column; 则子元素的排列方式为竖向：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 2.3 flex-wrap

> 属性说明：用来设置子元素是否换行，默认不换行。

属性值:

  * nowrap：不换行
  * wrap：换行

例：这里设置弹性容器总宽度600px，3个子元素的宽度都是300px。虽然子元素的总宽度超过了弹性容器的宽度，但是因为弹性容器默认不换行，所以这三个元素仍然会排列在一行。

```
<!DOCTYPE html>  
<html lang="en">  
<head>  
  <meta charset="UTF-8">  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">  
  <title>flex弹性布局</title>  
  <style>  
    .father {  
      width: 600px;  
      height: 200px;  
      margin: 0 auto;  
      background-color: gainsboro;  
      display: flex;  
    }  
    .son {  
      width: 300px;  
      height: 100px;  
    }  
  
    .son:nth-child(1) {  
      background-color: red;  
    }  
  
    .son:nth-child(2) {  
      background-color: green;  
    }  
  
    .son:nth-child(3) {  
      background-color: blue;  
    }  
  </style>  
</head>  
  
<body>  
  <div class="father">  
    <div class="son">1. 知否技术(公zhong号)</div>  
    <div class="son">2. flex布局</div>  
    <div class="son">3. 弹性盒子</div>  
  </div>  
</body>  
  
</html>  

```

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

设置换行之后，第三个元素就会跑到下一行：

```
  .father {  
      width: 600px;  
      height: 200px;  
      margin: 0 auto;  
      background-color: gainsboro;  
      display: flex;  
      flex-wrap: wrap; /* 设置换行 */  
    }  

```

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 2.4 align-items

> align-items：在弹性容器设置子元素**不换行** 的情况下，设置侧轴上的子元素排列方式。

属性值：

  * flex-start
  * flex-end
  * center
  * stretch：拉伸填充，默认值。

这里主轴默认是 X 轴，侧轴是 Y 轴。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 2.5 align-content

> align-content：在弹性容器设置子元素**换行** 的情况下， 设置侧轴上的子元素排列方式

属性值：

  * flex-start
  * flex-end
  * center
  * stretch：默认
  * space-between
  * space-around

这里主轴默认是 X 轴，侧轴是 Y 轴。![图片](data:image/svg+xml,%3C%3Fxml version='1.0'
encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1'
version='1.1' xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 2.6 flex-flow

> flex-flow：flex-direction 和  flex-wrap 的结合体
```
  flex-flow: column nowrap;  

```

## 3.子元素属性

### 3.1 flex

> flex：子元素占的剩余空间的份数，默认值是 0

例一：三个子元素 flex 都设置为1

```
  <style>  
    .father {  
      width: 800px;  
      height: 400px;  
      background-color: rgb(252, 204, 72);  
      margin: 0 auto;  
      display: flex;  
      color: white;  
      text-align: center;  
    }  
    .son {  
      height: 100px;  
      flex: 1;  
    }  
    .son:nth-child(1) {  
      background-color: red;  
    }  
    .son:nth-child(2) {  
      background-color: blue;  
    }  
    .son:nth-child(3) {  
      background-color: green;  
    }  
  </style>  
  <div class="father">  
    <div class="son">1</div>  
    <div class="son">2</div>  
    <div class="son">3</div>  
  </div>  

```

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

例二：只给第二个子元素设置 flex 值，第二个元素的宽度就是弹性的。

```
 <style>  
    .father {  
      width: 100%;  
      height: 400px;  
      background-color: rgb(252, 204, 72);  
      margin: 0 auto;  
      display: flex;  
      color: white;  
      text-align: center;  
    }  
    .son:nth-child(1) {  
      width: 100px;  
      background-color: red;  
    }  
    .son:nth-child(2) {  
      flex: 1;  
      background-color: blue;  
    }  
  
    .son:nth-child(3) {  
      width: 100px;  
      background-color: green;  
    }  
  </style>  
  <div class="father">  
    <div class="son">1</div>  
    <div class="son">2</div>  
    <div class="son">3</div>  
  </div>  

```

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 3.2 align-self

> align-self: 子元素在侧轴上的对齐方式

属性值：

  * flex-start
  * flex-end
  * center
  * stretch

这里主轴默认是 X 轴，侧轴是 Y 轴。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)![图片](data:image/svg+xml,%3C%3Fxml
version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0
0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)![图片](data:image/svg+xml,%3C%3Fxml
version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0
0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)![图片](data:image/svg+xml,%3C%3Fxml
version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0
0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 3.3 order

> order: 子元素的排列顺序，数值越小，越靠前。默认值是 0

例：第二个元素 order 设置负值，优先在前面显示。

```
<style>  
    .father {  
      width: 800px;  
      height: 400px;  
      background-color: gray;  
      margin: 0 auto;  
      display: flex;  
      color: white;  
      text-align: center;  
    }  
    .son {  
      flex: 1;  
    }  
    .son:nth-child(1) {  
      background-color: red;  
    }  
    .son:nth-child(2) {  
      background-color: blue;  
      order: -2;  
    }  
    .son:nth-child(3) {  
      background-color: green;  
    }  
</style>  
  <div class="father">  
    <div class="son">1</div>  
    <div class="son">2</div>  
    <div class="son">3</div>  
  </div>  

```

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg
width='1px' height='1px' viewBox='0 0 1 1' version='1.1'
xmlns='http://www.w3.org/2000/svg'
xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg
stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-
opacity='0'%3E%3Cg transform='translate\(-249.000000, -126.000000\)'
fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1'
height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

