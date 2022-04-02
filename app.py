#!/usr/bin/env python
# coding: utf-8

# In[21]:


from flask import Flask


# In[22]:


from textblob import TextBlob


# In[23]:


app = Flask(__name__)


# In[24]:


from flask import request, render_template

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        s = TextBlob(text).sentiment
        return(render_template("index.html",result = s))
    else:
        return(render_tempalte("index.html",result = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




