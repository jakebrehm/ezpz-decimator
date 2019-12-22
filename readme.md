<p align="center">
  <img src="https://github.com/jakebrehm/ezpz-decimator/blob/master/Assets/logo.png" width="558" height="126" alt="EZPZ Plotting Logo"/>
</p>

---

**EZPZ Decimator** is a simple program in the EZPZ family of programs that concatenates and then decimates one or more csv files. The files are specified by the user, as well as the number of header rows and the decimation factor.

# How to get it

To get a copy of this script, use the following command:
```
git clone https://github.com/jakebrehm/ezpz-decimator.git
```

# How to use it

In order to launch the program, open *EZPZ Decimator.exe* or run the source code via the command:

```
python decimator.py
```

First, you must specify that files that you want to concatenate and/or decimate. To do this, click the `Browse...` button of the `Input location` field and select one or more files.

Similarly, click the `Browse...` button of the `Output destination` field to choose where you want the resulting file to be saved.

Next, specify how many header rows are in your data. Note that each of your data files must be formatted the same way, meaning that **each file must have the same number of header rows.**

Specify the decimation factor in the `Decimation factor` field. Another way to think of this is "*I want to keep 1 out of every _ rows of data*", where the *_* is your decimation factor.

You can also choose whether or not to include the header information in the output file by toggling the `Include headers` checkbutton appropriately.

When you're ready, press the `Reduce` button. Navigate to the specified output destination to find the resulting file.

# Ideas for future changes
- Change the name to EZPZ Reducer
- Allow the user to reorder the inputs
- Add the ability to specify files multiple times in order to allow for the input files to be in different locations
- Show all of the inputs in a listbox instead of a basic entry field

---

# Authors
- **Jake Brehm** - *Initial Work* - [Email](mailto:jbrehm@tactair.com) | [Github](http://github.com/jakebrehm) | [LinkedIn](http://linkedin.com/in/jacobbrehm)