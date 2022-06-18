# AU School Handwriting Fonts

The AU School Handwriting Fonts are a variable typeface family designed specifically to meet Australian education standards. While carefully crafted to work well in a classroom environment, the fonts are handy outside the classroom as well.

The initial weight of the AU font-sets is intended to imitate the pencil thickness of actual handwriting, however they may be adjusted as desired in your usual word processor, or they can be used in software that supports variable fonts (such as Adobe) to make full use of alternate glyphs for transitional handwriting stages between grades 1 and 3.

![[link|width=400px]](https://user-images.githubusercontent.com/34974280/174439881-58459016-de6c-4157-b1f7-daa7bdd160c4.png "Regular")

![[link|width=400px]](https://user-images.githubusercontent.com/34974280/174439884-ef3fcedd-e528-4305-bf4f-0617badb77ce.png "Bold")

AU School Handwriting Fonts are purposefully designed with minimal under and over shoot at Cap Height, X-Height, Baseline and Descender making them perfect for use by teachers.

![[link|width=400px]](https://user-images.githubusercontent.com/34974280/159198981-e06b4972-3e52-4065-a402-58fd5b1ba301.png "NSW Ruled Exercise Book")

## Description ##

In lower primary school some Australian States teach different handwriting styles, while some States share the same style. The handwriting styles expected by each State's Education Department are as follows:

State | Style Name | Link
| :--- | :--- | :---
Queensland (QLD)  | QBeginners Print & QBeginners Pre-Cursive | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/QLD-School-Fonts "Read more")
New South Wales (NSW) | Foundation Print & Foundation Pre-Cursive | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/NSW-ACT-School-Fonts "Read more")
Tasmania (TAS) | Beginner Print & Pre-Cursive Print | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/TAS-School-Fonts "Read more")
Australian Capital Territory (ACT) | Foundation Print & Foundation Pre-Cursive |  [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/NSW-ACT-School-Fonts "Read more")
Victoria (VIC) | Print & Infant Cursive | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")
Northern Territory (NT) | Print & Infant Cursive | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")
Western Australia (WA) | Print & Infant Cursive | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/VIC-WA-NT-School-fonts "Read more")
South Australia (SA) | Beginner Print & Pre-Cursive Print | [Read more](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/tree/main/SA-School-Fonts "Read more")

## View and/or Install the Fonts ##

Click the link above matching the Australian State that you live in. 

1. Download the .zip file and unpack it. 
2. Double-click the .html file.
3. Adjust the sliders at the top of the page.

![Font Viewer](https://user-images.githubusercontent.com/34974280/174446978-9288fcce-d94a-43e5-90e3-2094f2c951fa.png)

To install the fonts choose an option:

<details>
  <summary>Windows</summary>
	<p>1. Open the Windows Control Panel.</br>
	2. Select Appearance and Personalization.</br>
	3. At the bottom, select Fonts.</br>
	4. To add a font, simply drag the .ttf file into the font window.</br>
	5. Click Yes when prompted.</p>
</details>
<details>
  <summary>Mac</summary>
	<p>1. Double-click the .ttf file</br>
	2. Click Install Font in the font preview window</br>
	3. After validation, it will open in the Font Book app</p>
</details>

- - - -

# About This Project #

This project contains the binary font files for all Australian states. Each family's subdirectory contains the .ttf font file sets, the source files and a .zip file to locally test the font in a variable font viewer without installing.

## Build from gftool ##

You can build the font locally, after cloning this repository.

```
1. At the root of your local clone (cd path/to/local/clone), create a virtual environment: python3 -m venv env

2. Activate the virtual env: source env/bin/activate

3. Install gftools (or the requirements) in the virtual env: pip install gftools

4. go to the "sources" directory and from the terminal, run : gftools builder config.yaml
```

## Bugs & Improvements ##

These fonts are the result of a collaborative project, where you are invited to discuss issues and even contribute to their ongoing development.

If you find a problem with a font file or have a request for the future development of its cursive counterpart, [please create a new issue in this project's issue tracker](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/issues "Go to the issue tracker").

## 

- - - -

# Acknowledgements & Credits #

- Santiago Orozco
- David Berlow
- Rosalie Wagner
- Corey Anderson
- Tina Anderson

- - - -

# Changelog #

**June 2022**

Date          | Description
------------- | -------------
Jun 18, 2022  | First release

- - - -

# License #

Copyright (c) 2022 The AU School Handwriting Fonts Project Authors (https://github.com/MezMerrit/AU-School-Handwriting-Fonts)

These Fonts are licensed under the SIL Open Font License, Version 1.1. This license is copied [Nhere](https://github.com/MezMerrit/AU-School-Handwriting-Fonts/blob/main/OFL.txt "SIL Open Font License"), and is also available with a FAQ at: https://scripts.sil.org/OFL.

The fonts files themselves also contain licensing and authorship metadata.
