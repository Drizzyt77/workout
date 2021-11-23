import json
import time

import PySimpleGUIQt as sg
from icecream import ic
import mysql.connector


def connect_sql():
    global cursor
    global mydb
    mydb = mysql.connector.connect(
        host="47.41.184.187",
        user="workout",
        password="workout",
        database="workout"
    )
    mycursor = mydb.cursor()
    cursor = mycursor
    mydb = mydb


def get_weeks():
    weeks = ["Week 1", 'Week 2', "Week 3"]
    return weeks


def get_check_state(key, week):
    if week is None:
        return False
    print(key)

    if week == 'Week 2':
        return False

    return True


def update_checkbox(box, value, week):
    print(box, value, week)
    time.sleep(.25)
    sql = 'SELECT boxes FROM checkstates WHERE week = %s'
    val = (week,)
    cursor.execute(sql, val)
    results = cursor.fetchone()
    cur_boxes = json.loads(results[0])
    print(cur_boxes)
    cur_boxes[box] = value
    cur_boxes = json.dumps(cur_boxes)
    time.sleep(.25)
    print(cur_boxes)
    sql = 'UPDATE checkstates SET boxes = %s WHERE week = %s'
    val = (str(cur_boxes), week,)
    cursor.execute(sql, val)
    mydb.commit()
    return cur_boxes


def my_popup(window):
    layout = [
        [sg.Text("Here's the \nuser-defined \npopup !!!")],
        [sg.Button("OK", key='OK'), sg.Button("CANCEL")]
    ]
    win = sg.Window("My Popup", layout, keep_on_top=True)

    event, value = win.read()
    if event == sg.WINDOW_CLOSED or event == 'OK':
        event = "CANCEL"
    win.close()


cursor = None
mydb = None

full_categories = ['-SUBRUSH-', '-MBRUSH-', '-TUBRUSH-', '-WBRUSH-', '-THBRUSH-', '-FBRUSH-', '-SABRUSH-',
                   '-SUSKIN-', '-MSKIN-', '-TUSKIN-', '-WSKIN-', '-THSKIN-', '-FSKIN-', '-SASKIN-',
                   '-SUDISHES-', '-MDISHES-', '-TUDISHES-', '-WDISHES-', '-THDISHES-', '-FDISHES-',
                   '-SADISHES-', '-SUCLEAN-', '-MCLEAN-', '-TUCLEAN-', '-WCLEAN-', '-THCLEAN-', '-FCLEAN-',
                   '-SACLEAN-', '-SUPET-', '-MPET-', '-TUPET-', '-WPET-', '-THPET-', '-FPET-', '-SAPET-',
                   '-SULAUNDRY-', '-MLAUNDRY-', '-TULAUNDRY-', '-WLAUNDRY-', '-THLAUNDRY-', '-FLAUNDRY-',
                   '-SALAUNDRY-', '-SUFOOD-', '-MFOOD-', '-TUFOOD-', '-WFOOD-', '-THFOOD-', '-FFOOD-',
                   '-SAFOOD-', '-SUDONECHECK-', '-MDONECHECK-', '-TUDONECHECK-', '-WDONECHECK-', '-THDONECHECK-',
                   '-FDONECHECK-', '-SADONECHECK-']


def main():
    global cursor
    global mydb
    connect_sql()
    cur_week = None
    table_values = [["Test", "Test2", 'Test3', "Test4"],
                    ["Test", "Test2", 'Test3', "Test4"],
                    ["Test", "Test2", 'Test3', "Test4"],
                    ["Test", "Test2", 'Test3', "Test4"]]
    text = [
        [
            sg.Text("Workout Tracker", justification='center', text_color='purple')
        ],
        [
            sg.Button("Add Workout Time", key='-TEST-', enable_events=True)
        ],
        [
            sg.Combo(values=get_weeks(), readonly=True, size=(10, .5), enable_events=True, key='-WEEK_SELECT-')
        ]
    ]
    box_text = [
        [
            sg.Text("Categories")
        ],
        [
            sg.HSeperator()
        ],
        [
            sg.Text("Brush Teeth", margins=(0, 0, 0, 1))
        ],
        [
            sg.Text("Skin Care", margins=(0, 0, 0, 1))
        ],
        [
            sg.Text("Dishes", margins=(0, 0, 0, 1))
        ],
        [
            sg.Text("Pet Care", margins=(0, 0, 0, 1))
        ],
        [
            sg.Text("Clean", margins=(0, 0, 0, 1))
        ],
        [
            sg.Text("Laundry", margins=(0, 0, 0, 1))
        ],
        [
            sg.Text("Food Goal", margins=(0, 0, 0, 1))
        ],
        [
            sg.Text("Done", margins=(0, 0, 0, 1))
        ]
    ]
    boxes = [
        [
            sg.Text("Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday")
        ],
        [
            sg.HSeperator()
        ],
        [
            sg.Checkbox("", key='-SUBRUSH-', enable_events=True),
            sg.Checkbox("", key='-MBRUSH-', enable_events=True),
            sg.Checkbox("", key='-TUBRUSH-', enable_events=True),
            sg.Checkbox("", key='-WBRUSH-', enable_events=True),
            sg.Checkbox("", key='-THBRUSH-', enable_events=True),
            sg.Checkbox("", key='-FBRUSH-', enable_events=True),
            sg.Checkbox("", key='-SABRUSH-', enable_events=True)
        ],
        [
            sg.Checkbox("", key='-SUSKIN-', enable_events=True),
            sg.Checkbox("", key='-MSKIN-', enable_events=True),
            sg.Checkbox("", key='-TUSKIN-', enable_events=True),
            sg.Checkbox("", key='-WSKIN-', enable_events=True),
            sg.Checkbox("", key='-THSKIN-', enable_events=True),
            sg.Checkbox("", key='-FSKIN-', enable_events=True),
            sg.Checkbox("", key='-SASKIN-', enable_events=True)
        ],
        [
            sg.Checkbox("", key='-SUDISHES-', enable_events=True),
            sg.Checkbox("", key='-MDISHES-', enable_events=True),
            sg.Checkbox("", key='-TUDISHES-', enable_events=True),
            sg.Checkbox("", key='-WDISHES-', enable_events=True),
            sg.Checkbox("", key='-THDISHES-', enable_events=True),
            sg.Checkbox("", key='-FDISHES-', enable_events=True),
            sg.Checkbox("", key='-SADISHES-', enable_events=True)
        ],
        [
            sg.Checkbox("", key='-SUCLEAN-', enable_events=True),
            sg.Checkbox("", key='-MCLEAN-', enable_events=True),
            sg.Checkbox("", key='-TUCLEAN-', enable_events=True),
            sg.Checkbox("", key='-WCLEAN-', enable_events=True),
            sg.Checkbox("", key='-THCLEAN-', enable_events=True),
            sg.Checkbox("", key='-FCLEAN-', enable_events=True),
            sg.Checkbox("", key='-SACLEAN-', enable_events=True)
        ],
        [
            sg.Checkbox("", key='-SUPET-', enable_events=True),
            sg.Checkbox("", key='-MPET-', enable_events=True),
            sg.Checkbox("", key='-TUPET-', enable_events=True),
            sg.Checkbox("", key='-WPET-', enable_events=True),
            sg.Checkbox("", key='-THPET-', enable_events=True),
            sg.Checkbox("", key='-FPET-', enable_events=True),
            sg.Checkbox("", key='-SAPET-', enable_events=True)
        ],
        [
            sg.Checkbox("", key='-SULAUNDRY-', enable_events=True),
            sg.Checkbox("", key='-MLAUNDRY-', enable_events=True),
            sg.Checkbox("", key='-TULAUNDRY-', enable_events=True),
            sg.Checkbox("", key='-WLAUNDRY-', enable_events=True),
            sg.Checkbox("", key='-THLAUNDRY-', enable_events=True),
            sg.Checkbox("", key='-FLAUNDRY-', enable_events=True),
            sg.Checkbox("", key='-SALAUNDRY-', enable_events=True)
        ],
        [
            sg.Checkbox("", key='-SUFOOD-', enable_events=True),
            sg.Checkbox("", key='-MFOOD-', enable_events=True),
            sg.Checkbox("", key='-TUFOOD-', enable_events=True),
            sg.Checkbox("", key='-WFOOD-', enable_events=True),
            sg.Checkbox("", key='-THFOOD-', enable_events=True),
            sg.Checkbox("", key='-FFOOD-', enable_events=True),
            sg.Checkbox("", key='-SAFOOD-', enable_events=True)
        ],
        [
            sg.Checkbox("", key='-SUDONECHECK-', enable_events=True),
            sg.Checkbox("", key='-MDONECHECK-', enable_events=True),
            sg.Checkbox("", key='-TUDONECHECK-', enable_events=True),
            sg.Checkbox("", key='-WDONECHECK-', enable_events=True),
            sg.Checkbox("", key='-THDONECHECK-', enable_events=True),
            sg.Checkbox("", key='-FDONECHECK-', enable_events=True),
            sg.Checkbox("", key='-SADONECHECK-', enable_events=True)
        ]
    ]
    layout = [
        [
            sg.Column(text)
        ],
        [
            sg.Column(box_text, element_justification='l'),
            sg.VSeperator(),
            sg.Column(boxes)
        ]
    ]
    window = sg.Window("Workout Tracker", layout=layout)
    while True:
        event, values = window.read(timeout=5000, timeout_key='-REFRESH-')
        ic(event)
        ic(cursor)
        # ic(event, values)
        if event == '-TEST-':
            my_popup(window)

        elif event == '-WEEK_SELECT-':
            if values['-WEEK_SELECT-'] is not None:
                cur_week = values['-WEEK_SELECT-']
                sql = 'SELECT boxes FROM checkstates WHERE week = %s'
                val = (cur_week,)
                connect_sql()
                cursor.execute(sql, val)
                results = cursor.fetchone()
                mydb.commit()
                ic(results, results[0])
                results2 = json.loads(results[0])
                for key in results2.keys():
                    window[key].update(results2[key])

        elif event in full_categories:
            update_checkbox(event, values[event], cur_week)
        elif event == '-REFRESH-':
            cur_week = values['-WEEK_SELECT-']
            sql = 'SELECT boxes FROM checkstates WHERE week = %s'
            val = (cur_week,)
            cursor.execute(sql, val)
            results = cursor.fetchone()
            results2 = json.loads(results[0])
            mydb.commit()
            print(results2)
            for key in results2.keys():
                window[key].update(results2[key])
            continue
        elif event == sg.WINDOW_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    main()
