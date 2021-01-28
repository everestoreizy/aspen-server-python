from flask import Flask, render_template, g, url_for

class Item:
    def __init__(self, id, content, content2, completed, planned_date, due_date):
        self.id = id
        self.content = content #assignment title, too lazy to refactor
        self.content2 = content2 #assignment description
        self.completed = completed
        self.planned_date = planned_date
        self.due_date = due_date
        self.due_date_str = date_to_string(due_date)
        # self.img_src = url_for('static', filename='images/check-filled.png') if self.completed else url_for('static', filename='images/check-unfilled.png')
    def compare_to(self, other):
        if(self.id == other.id):
            return True
        else:
            return False

class ItemCollection:
    def __init__(self, date, items):
        self.date = date
        self.date_str = date_to_string(self.date)
        self.items = items
        # self.img_plus_url = url_for('static', filename='images/plus.png')
    def add_item(self, item):
        self.items.append(item)
    def render(self):
        # g.date = self.date_to_string(self.date)
        # content_html = ""
        # for item in self.items: content_html += item.render()
        # g.content = content_html
        # g.img_plus_url = url_for('static', filename='images/plus.png')
        # return render_template('list.html')
        print("Deprecated function")

def date_to_string(dt):
    return dt.strftime('%A') + ", " + dt.strftime('%b') + ". " + str(dt.day)

def sort_items(item_list):
    item_list.sort(key=get_planned_date)
    print(item_list)
    ics = [ ]
    ics.append(ItemCollection(item_list[0].planned_date, []))
    for item in item_list:
        if item.planned_date != ics[-1].date:
            print(date_to_string(item.planned_date) + "!=" + date_to_string(ics[-1].date))
            ics.append(ItemCollection(item.planned_date, [item]))
        else:
            ics[-1].add_item(item)
    return ics


def get_planned_date(i):
    return i.planned_date