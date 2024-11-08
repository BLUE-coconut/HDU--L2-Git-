# HDU华为智能基座社团-第二次授课项目
## An Open-Cv task and Tutorial to Convert the given image to Cartoon and Pencil Sketch
Oringinal Repositories: [link](https://github.com/AswinSampath1401/Pencil-and-Cartoon-Effects)


# 使用方法说明
1. 安装依赖：在当前环境中检测是否含有`matplotlib`和`opencv-python`包。若缺少，则安装所缺的包。
2. 运行demo：首先将需要处理的图像放置inputs文件夹下
- 终端命令行输入`python cartoonify_demo.py`生成卡通画风格的图片（保存在outputs文件夹下）
- 终端命令行输入`python pencilSketch_demo.py`生成铅笔素描风格的图片（保存在outputs文件夹下）

## Cartoon Effect 

### Aim <br>

To cartoonize an Image by lightenting the colors and detecting sharp edges

### Procedure
Blur the image thereby lightening the colors and apply suitable filters to detect sharp edges 

### Methodology<br>
<b><u>To Lighten the Imgae</i></u></b>
<li><i>Blur The Image using Bilateral Filter</i></li><br>

<b><u> To Detect Sharp Edges</u></b>
<li><i>Convert Image to grayscale</i></li>
<li><i>Apply Median Blur to blur the Image</i></li>
<li><i>Apply Apaptive Treshold for a min_treshold which opencv adjusts automatically</i></li>
<li><i>Edges are finally obtained from Adaptive Treshold</i></li>
<br>

### <b><u>Final  Result</b></u>
<li><i>Bitwise And of the Image with Sharp edges and Blurred Color image will give us a nice Cartoonized Image</i></li>
<br>

### <a href='Markdown\Demo.md'>Click here to see demo</a>
<br>

## Pencil Effect 

### Aim <br>

To create a pencil Sketch of an Image by using basic filters

### Procedure
Apply Image Blending Techniques such as Dodging and Burning and we are good to go.

### Methodology<br>
<li><i>Convert the given image into grayscale</i></li>
<li><i> Invert the grayscale to get negative image</i></li>
<li><i>Apply Gaussian Blur to the negative image</i></li>
<li><i>Blend the grayscale image(we got from rgb image in step 1) with the blurred negative image using a color dodge</i></li>
<br>

### <b><u>Final  Result</b></u>
<li><i>A nice Pencil Sketch is generated</i></li> 
<hr>

### <a href='Markdown\PencilDemo.md'>Click here to see demo</a>
