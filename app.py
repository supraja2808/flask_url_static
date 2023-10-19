from flask import Flask,render_template

FAI=Flask(__name__)

#collecting the data 
@FAI.route('/wish/<name>')

def wish(name):
    return f'hi {name} how are u'


@FAI.route('/first')
def first():
    return render_template('first.html')

@FAI.route('/second')
def second():
    return render_template('second.html')






if __name__=='__main__':
    FAI.run(debug=True,host='127.0.0.1',port='5001')