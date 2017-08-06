# Filtering

A lot of image processing algorithms rely on the convolution between a kernel (typicaly a 3x3 or 5x5 matrix) and an image. This may sound scary to some of you but that's not as difficult as it sounds:

Let's take a 3x3 matrix as our kernel. For each pixel, the filter multiplies the current pixel value and the other 8 surrounding pixels by the kernel corresponding value. Then it adds the result to get the value of the current pixel. That's all. Let's see an example:

<div style="display: flex">
	<table>
		<tr><td>7</td> <td>23</td><td>50</td><td>64</td><td>14</td></tr>
		<tr><td>15</td><td>13</td><td>31</td><td>46</td><td>8</td></tr>
		<tr><td>42</td><td>25</td><td>92</td><td>31</td><td>32</td></tr>
		<tr><td>71</td><td>44</td><td>74</td><td>94</td><td>92</td></tr>
		<tr><td>2</td> <td>43</td><td>51</td><td>35</td><td>4</td></tr>
	</table>
	<span style="font-size: 32px">
		X
	</span>
	<table>
		<tr><td>0</td><td>2</td><td>0</td></tr>
		<tr><td>0</td><td>2</td><td>0</td></tr>
		<tr><td>0</td><td>2</td><td>0</td></tr>
	</table>
</div>

## Edge detection

@[Sobel operator]({"stubs": ["edge/sobel.py"], "command": "sh -c 'cp lena.png input.png && python3 edge/sobel.py && echo \"TECHIO> open -s /project/target/ index.html\"'"})
