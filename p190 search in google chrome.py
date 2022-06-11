# first import the module
import webbrowser

# then make a url variable
value=input("Enter search ")
url = "https://www.google.com/search?q="+value

# then call the default open method described above
webbrowser.open(url)
