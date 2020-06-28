<div align="center">

  <img src="https://github.com/jakebrehm/ezpz-reducer/blob/master/Assets/logo.png" alt="EZPZ Plotting Logo"/>

  <br>
  <br>

  <h1>Concatenates and then decimates one or more csv files.</h1>

  <br>

  <img src="https://img.shields.io/github/last-commit/jakebrehm/ezpz-reducer?style=for-the-badge&color=violet" alt="Last Commit"></img>
  <img src="https://img.shields.io/github/commit-activity/w/jakebrehm/ezpz-reducer?style=for-the-badge&color=violet" alt="Commit Activity"></img>
  <img src="https://img.shields.io/github/license/jakebrehm/ezpz-reducer?style=for-the-badge&color=violet" alt="MIT License"></img>
  <br>
  <img src="https://img.shields.io/badge/Made%20With-Python%203.7-violet.svg?style=for-the-badge&logo=Python" alt="Made with Python 3.7"></img>

</div>


## What is it?

**EZPZ Reducer** is a simple tool in the EZPZ family of programs that concatenates and then decimates one or more csv files. The files are specified by the user, as well as the number of header rows and the decimation factor.

## How do I get it?

It is most convenient to download the latest executable file release, which can be found [here](https://github.com/jakebrehm/ezpz-reducer/releases/latest).

Otherwise, if you want to run the program via the source code, use the following command:
```
git clone https://github.com/jakebrehm/ezpz-reducer.git
```

## How do I use it?

In order to launch the program, open *EZPZ Reducer.exe* or run the source code via the command:

```
python main.py
```

First, you must specify that files that you want to concatenate and/or decimate. To do this, click the `Browse...` button of the `Input location` field and select one or more files.

Similarly, click the `Browse...` button of the `Output destination` field to choose where you want the resulting file to be saved.

Next, specify how many header rows are in your data. Note that each of your data files must be formatted the same way, meaning that **each file must have the same number of header rows.**

Specify the decimation factor in the `Decimation factor` field. Another way to think of this is "*I want to keep 1 out of every _ rows of data*", where the *_* is your decimation factor.

You can also choose whether or not to include the header information in the output file by toggling the `Include headers` checkbutton appropriately.

When you're ready, press the `Reduce` button. Navigate to the specified output destination to find the resulting file.

## Ideas for future changes
- Allow the user to reorder the inputs
- Make the program work with delimiters other than a comma
- Add the ability to specify files multiple times in order to allow for the input files to be in different locations
- Show all of the inputs in a listbox instead of a basic entry field
- Add validation to the entry boxes to only allow integer values (or use a spinbox)

---

## Authors
- **Jake Brehm** - *Initial Work* - [Email](mailto:jbrehm@tactair.com) | [Github](http://github.com/jakebrehm) | [LinkedIn](http://linkedin.com/in/jacobbrehm)