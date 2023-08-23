import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import datetime
current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(
  current_dir, "testdb.sqilte3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

card_number = 1


#database model
class User(db.Model):
  __tablename__ = "user"
  id = db.Column(db.Integer, autoincrement=True)
  firstname = db.Column(db.String)
  lastname = db.Column(db.String)
  username = db.Column(db.String,
                       unique=True,
                       primary_key=True,
                       nullable=False)
  password = db.Column(db.String, nullable=False, unique=True)


class Lists(db.Model):
  __tablename__ = "lists"
  list_id = db.Column(db.Integer,
                      autoincrement=True,
                      primary_key=True,
                      unique=True)
  list_title = db.Column(db.String, nullable=False)
  list_description = db.Column(db.String)


class Cards(db.Model):
  __tablename__ = "cards"
  card_id = db.Column(db.Integer,
                      autoincrement=True,
                      primary_key=True,
                      nullable=False,
                      unique=True)
  card_title = db.Column(db.String, nullable=False, unique=True)
  card_status = db.Column(db.String)
  card_deadline = db.Column(db.DateTime)
  card_description = db.Column(db.String)
  date_and_time = db.Column(db.String)
  date_updated = db.Column(db.String)
  time_completed = db.Column(db.String)
  list_id = db.Column(db.Integer, db.ForeignKey("lists.list_id"))


db.create_all()

#add info to database


@app.route("/", methods=["GET", "POST"])
def login_get():
  return render_template("login.html")


#create account
@app.route("/api/create/account", methods=["POST"])
def create_account():
  try:
    register_firstname = request.form['rfirstname']
    register_lastname = request.form['rlastname']
    register_username = request.form['rusername']
    register_password = request.form['rpassword']
    new_user = User(firstname=register_firstname,lastname=register_lastname,username=register_username,password=register_password)
    db.session.add(new_user)
    db.session.commit()
    return render_template("login.html")
  except:
    return render_template("login.html")



#add list
@app.route("/api/list/new", methods=["POST"])
def add_list():
  try:
    l_title = request.form['ltitle']
    ldescription = request.form['ldescription']
    new_list = Lists(list_title=l_title, list_description=ldescription)
    db.session.add(new_list)
    db.session.commit()
    cardall = Cards.query.all()
    listall = Lists.query.all()
    return render_template('homepage.html', listall=listall, cardall=cardall, today = datetime.datetime.now())
  except:
    return "Invalid Input"


#add card
@app.route("/api/card/new", methods=["POST"])
def add_card():
  try:
    c_title = request.form['ctitle']
    c_status = request.form['cstatus']
    c_deadline = request.form['cdeadline']
    c_description = request.form['cdescription']
    list_number = request.form['clistnumber']
    new_card = Cards(card_title=c_title,
                     card_status=c_status,
                     card_deadline=datetime.datetime.strptime(c_deadline, '%d-%m-%Y').date(),
                     card_description=c_description,
                     date_and_time=datetime.datetime.now(),
                     date_updated=datetime.datetime.now(),
                     time_completed='',
                     list_id=list_number)
    db.session.add(new_card)
    db.session.commit()
    cardall = Cards.query.all()
    listall = Lists.query.all()
    return render_template('homepage.html', listall=listall, cardall=cardall, today = datetime.datetime.now())
  except:
      return "Invalid input"


#delete info from database
#@app.route("/delete_user", methods=["DELETE"])
#@app.route("/api/list/<list_id>", methods=["DELETE"])
#@app.route("/api/card/<card_id>", methods=["DELETE])


#delete card
@app.route("/deltask", methods=["GET", "POST"])
def del_task():
  return render_template("delcard.html")


@app.route("/api/card/remove", methods=["POST"])
def remove_card():
  try:
    cr_title = request.form['crtitle']
    waste_card = Cards.query.filter_by(card_title=cr_title).one()
    db.session.delete(waste_card)
    db.session.commit()
    cardall = Cards.query.all()
    listall = Lists.query.all()
    return render_template('homepage.html', listall=listall, cardall=cardall, today = datetime.datetime.now())
  except:
    return "No such record found"


#delete list
@app.route("/dellist", methods=["GET", "POST"])
def del_list():
  return render_template("dellist.html")


@app.route("/api/list/delete", methods=["POST"])
def remove_list():
  try:
    lr_title = request.form['lrtitle']
    waste_list = Lists.query.filter_by(list_title=lr_title).one()
    db.session.delete(waste_list)
    db.session.commit()
    cardall = Cards.query.all()
    listall = Lists.query.all()
    return render_template('homepage.html', listall=listall, cardall=cardall, today = datetime.datetime.now())
  except:
    return "No such record found"


#edit card
@app.route("/api/card/edit", methods=["GET", "POST"])
def edit_card():
  try:
    c_old_title = request.form['coldtitle']
    card_edit = Cards.query.filter_by(card_title=c_old_title).one()
    card_edit.card_title = request.form['cnewtitle']
    card_edit.card_description = request.form['cnewcontent']
    card_edit.card_deadline = datetime.datetime.strptime(request.form['cnewdeadline'], '%d-%m-%Y').date()
    card_edit.card_status = request.form['cnewstatus']
    db.session.commit()
    cardall = Cards.query.all()
    listall = Lists.query.all()
    return render_template('homepage.html', listall=listall, cardall=cardall, today = datetime.datetime.now())
  except:
    return "No such record found"


#edit list
@app.route("/api/list/edit", methods=["GET", "POST"])
def edit_list():
  try:
    l_old_title = request.form['loldtitle']
    list_edit = Lists.query.filter_by(list_title=l_old_title).one()
    list_edit.list_title = request.form['lnewtitle']
    db.session.commit()
    cardall = Cards.query.all()
    listall = Lists.query.all()
    return render_template('homepage.html', listall=listall, cardall=cardall, today = datetime.datetime.now())
  except:
    return "No such record found"


#login
@app.route("/login", methods=["POST"])
def login():
  check_username = request.form['user_name']
  if User.query.filter_by(username=check_username) != None:
    user_record = User.query.filter_by(username=check_username).one()
    check_password = request.form['pass_word']
    if user_record.password == check_password:
      listall = Lists.query.all()
      cardall = Cards.query.all()
      return render_template("homepage.html",listall=listall,cardall=cardall, today = datetime.datetime.now())
    else:
      return "Incorrect Password"
  else:
    return "Invalid Username"




@app.route("/homepage", methods=["GET", "POST"])
def home():
  listall = Lists.query.all()
  cardall = Cards.query.all()
  return render_template("homepage.html", listall=listall, cardall=cardall, today = datetime.datetime.now())


@app.route("/create", methods=["GET", "POST"])
def create():
  return render_template("create_account.html")


@app.route("/createlist", methods=["GET"])
def add_list_get():
  return render_template("addlist.html")


@app.route("/createcard", methods=["GET"])
def add_card_get():
  return render_template("addtask.html")


@app.route("/editlist", methods=["GET"])
def edit_list_get():
  return render_template("editlist.html")


@app.route("/edittask", methods=["GET"])
def edit_task_get():
  return render_template("edittask.html")


@app.route("/home", methods=["GET", "POST"])
def home_page():
  listall = Lists.query.all()
  cardall = Cards.query.all()
  return render_template("home.html", listall=listall, cardall=cardall)


@app.route("/mark", methods=["GET"])
def mark_get():
  return render_template("mark.html")


@app.route("/mark", methods=["POST"])
def mark():
  try:
    c_old_title = request.form['coldtitle']
    print(c_old_title)
    if Cards.query.filter_by(card_title=c_old_title) != None:
      card_edit = Cards.query.filter_by(card_title=c_old_title).one()
      card_edit.card_status = "Done"
      card_edit.time_completed = datetime.datetime.now()
      db.session.commit()
    listall = Lists.query.all()
    cardall = Cards.query.all()
    return render_template("homepage.html", listall=listall, cardall=cardall, today = datetime.datetime.now())
  except:
    return "No such record found"


@app.route("/test", methods=["GET", "POST"])
def test():
  listall = Lists.query.all()
  cardall = Cards.query.all()
  return render_template("homepage1.html", listall=listall, cardall=cardall)


#plot graph
@app.route("/plot", methods=["GET","POST"])
def plot_graph():
  try:
    cards_per_list = {}
    crossed_deadline = 0
    listall = Lists.query.all()
    cardall = Cards.query.all()
    for alist in listall:
      tasks = 0
      for acard in cardall:
        if alist.list_id == acard.list_id:
          tasks += 1
      cards_per_list[alist.list_id] = tasks
    for card in cardall:
      if card.card_deadline < datetime.datetime.now():
        crossed_deadline += 1
    import matplotlib.pyplot as plt
    import numpy as np
    list_completed = []
    y_list = []
    cardall = Cards.query.all()
    for card in cardall:
      if card.time_completed != "":
        print(str(card.time_completed))
        list_completed.append(str(card.time_completed))
    for y in range(len(list_completed)):
      y_list.append(y + 1)

    plt.bar(np.array(list_completed),
            np.array(y_list),
            color='green',
            width=0.4)
    plt.xlabel('time')
    plt.ylabel('tasks completed')
    plt.title('xlabels() function')
    plt.savefig("static/output.jpg")
    no_of_tasks_completed = len(list_completed)
    return render_template("summary.html", cards_per_list=cards_per_list,  no_of_tasks_completed=no_of_tasks_completed, crossed_deadline=crossed_deadline)
  except:
    listall = Lists.query.all()
    cardall = Cards.query.all()
    return render_template("homepage.html", listall=listall, cardall=cardall, today = datetime.datetime.now())


if __name__ == '__main__':
  #Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=5000)
  plot_graph()
