from flask import Flask, render_template, request, url_for, redirect
import os, pandas


data_list = os.listdir('./data')

iris_data = pandas.read_csv("./data/iris/iris.csv")



app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts = data_list)


@app.route('/iris', methods = ['GET', 'POST'])
def iris_home():
	return render_template("iris_home.html", posts = iris_data)


@app.route('/clustering', methods = ['GET', 'POST'])
def iris_clustering():
	return render_template("iris_clustering.html")

@app.route('/iris', methods = ['GET', 'POST'])
def iris_cnn():
	return render_template("iris_cnn.html", posts = iris_data)


if __name__ == "__main__":
  app.run(debug = True)


