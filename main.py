from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont
import numpy as np
import pandas as pd
import difflib
from PIL import ImageTk,Image



window = Tk()
window.geometry("1280x720")
window.configure(bg = "#ffffff")

w_width = 1280
w_height = 720
s_width = window.winfo_screenwidth()
s_height = window.winfo_screenheight()
center_x = int(s_width/2 - w_width/2)
center_y = int(s_height/2 - w_height/2)
window.geometry(f'{w_width}x{w_height}+{center_x}+{center_y}')


#FRAME 2:
def open_frame2():
    frame1.forget()
    frame2.pack(fill = 'both', expand = 1)

#FRAME 3
def open_frame3():
    frame2.forget()
    frame3.pack(fill = 'both', expand = 1)

#FRAME 4
def open_frame4():
    frame3.forget()
    frame4.pack(fill = 'both', expand = 1)
    isa = Symptom1.get()
    # print (isa)
    dalawa = Symptom2.get()
    tatlo = Symptom3.get()
    apat = Symptom4.get()
    lima = Symptom5.get()
    combine_symp = ["SYMPTOM 01:",isa,"\nSYMPTOM 02:",dalawa,"\nSYMPTOM 03:",tatlo,"\nSYMPTOM 04:",apat,"\nSYMPTOM 05:",lima]
    sentence = ' '.join(combine_symp)
    print(sentence)
    label_symp.configure(text = sentence)

#FRAME 5
def open_frame5():
    frame4.forget()
    frame5.pack(fill = 'both', expand = 1)

    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()
        # DecisionTree()

#SIDEBAR FUNCTION
def toggle_win():
    f1=Frame(window,width=222,height=720,bg='#58AAEC')
    f1.place(x=0,y=0)

    def clicked():
        print("BUTTON CLICKED")

    #buttons
    def bttn(x,y,sze,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #58AAEC
            myButton1['foreground']= 'white'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= 'white'

        font1 = tkFont.Font(family='Raleway', size=sze, weight=tkFont.BOLD)
        myButton1 = Button(f1,text=text,
                        width=18,
                        height=2,
                        font=font1,
                        fg='white',
                        border=0,
                        bg=fcolor,
                        activeforeground='white',
                        activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,81,15,'D I A G N O S I S','#1471C9','#58AAEC',clicked)
    bttn(0,141,15,'R E C O R D S','#1471C9','#58AAEC',clicked)
    bttn(0,201,15,'S U M M A R Y','#1471C9','#58AAEC',clicked)

    #
    def dele():
        f1.destroy()

    #CLOSES SIDEBAR
    global closeimg
    closeimg = ImageTk.PhotoImage(Image.open("close.png"))
    closeb = Button(f1,
            image=closeimg,
            borderwidth = 0,
            highlightthickness = 0,
            command = dele,
            relief = "flat",
            activebackground = "#58AAEC",
            cursor = 'hand2')
    closeb.place(
        x=176, y=11,
        width = 38,
        height = 38)



def btn_clicked():
    print("Button Clicked")


frame1 = Frame(window)
frame1.pack(fill='both', expand=1)
frame2 = Frame(window)
frame3 = Frame(window)
frame4 = Frame (window)
frame5 = Frame (window)


l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)


#PREDICTION PART
def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    from sklearn.metrics import accuracy_score
    # y_pred = gnb.predict(X_test)
    # print("\n---------------------------------------------------------------------")
    # print(accuracy_score(y_test, y_pred))
    # print(accuracy_score(y_test, y_pred, normalize=False))
    # print("ACCURACY ACQUIRED\n---------------------------------------------------------------------")

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            print("PREDICTED DISEASE:", disease[a])
            break

    disease_data = pd.read_csv('f2.csv')

    list_of_all_titles = disease_data['disease'].tolist()
    
    find_close_match = difflib.get_close_matches(disease[a], list_of_all_titles, 30, cutoff=0.5)
    print(find_close_match)
    close_match = find_close_match[0]
    print(close_match)

    pd.options.display.max_colwidth = 3000
    disease_data.set_index("disease", inplace=True)
    disease_data.head()

    recommend = disease_data.loc[close_match]
    print(recommend)
    pd.options.display.max_colwidth = 3000


    if (h=='yes'):
        t3.delete("1.0", END)
        t4.delete("1.0", END)
        t3.insert(END, disease[a])
        t4.insert(END, recommend)
    else:
        t3.delete("1.0", END)
        t4.delete("1.0", END)
        t3.insert(END, "No Disease")


#-------------------FRAME1-------------------
f1_canvas0 = Canvas(
    frame1,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f1_canvas0.place(x = 0, y = 0)

f1_background_img0 = PhotoImage(file = f"f1-background0.png")
f1_background0 = f1_canvas0.create_image(
    640.0, 360.0,
    image=f1_background_img0)

f1_img0 = PhotoImage(file = f"f1-img0.png")
f1_b0 = Button(frame1,
    image = f1_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_frame2,
    relief = "flat",
    activebackground = "#1471C9",
    cursor = 'hand2')
f1_b0.place(
    x = 137, y = 507,
    width = 217,
    height = 65)

#-------------------FRAME2-------------------
f2_canvas1 = Canvas(
    frame2,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f2_canvas1.place(x = 0, y = 0)

f2_background_img1 = PhotoImage(file = f"f2-background1.png")
bf2_ackground1 = f2_canvas1.create_image(
    638.5, 360.0,
    image=f2_background_img1)

f2_img1 = PhotoImage(file = f"f2-img1.png")
f2_b1 = Button(frame2,
    image = f2_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = toggle_win,
    relief = "flat",
    activebackground = "#1471C9",
    cursor = 'hand2')
f2_b1.place(
    x = 37, y = 13,
    width = 49,
    height = 34)

f2_img2 = PhotoImage(file = f"f2-img2.png")
f2_b2 = Button(frame2,
    image = f2_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_frame3,
    relief = "flat",
    activebackground = "#FFFFFF",
    cursor = 'hand2')
f2_b2.place(
    x = 282, y = 522,
    width = 236,
    height = 78)

#-------------------FRAME3-------------------
OPTIONS = sorted(l1)
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)


f3_canvas = Canvas(
    frame3,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f3_canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"f3-background.png")
background = f3_canvas.create_image(
    640.0, 360.0,
    image=background_img)

f3_img0 = PhotoImage(file = f"f3-img0.png")
f3_b0 = Button(frame3,
    image = f3_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_frame4,
    relief = "flat",
    activebackground = "#FFFFFF",
    cursor = 'hand2')
f3_b0.place(
    x = 949, y = 632,
    width = 146,
    height = 60)

label_option = Label(frame3, text="")
label_option.place(x=242, y=290,
    width = 796,
    height = 303)

S1En = OptionMenu(label_option, Symptom1,*OPTIONS)
S1En.pack(ipadx=1, ipady=1,
          expand=True, fill='both')
S2En = OptionMenu(label_option, Symptom2,*OPTIONS)
S2En.pack(ipadx=1, ipady=1,
          expand=True, fill='both')
S3En = OptionMenu(label_option, Symptom3,*OPTIONS)
S3En.pack(ipadx=1, ipady=1,
          expand=True, fill='both')
S4En = OptionMenu(label_option, Symptom4,*OPTIONS)
S4En.pack(ipadx=1, ipady=1,
          expand=True, fill='both')
S5En = OptionMenu(label_option, Symptom5,*OPTIONS)
S5En.pack(ipadx=1, ipady=1,
          expand=True, fill='both')



f3_img1 = PhotoImage(file = f"f2-img1.png")
f3_b1 = Button(frame3,
    image = f2_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = toggle_win,
    relief = "flat",
    activebackground = "#1471C9",
    cursor = 'hand2')
f3_b1.place(
    x = 37, y = 13,
    width = 49,
    height = 34)


#-------------------FRAME4-------------------
f2_canvas = Canvas(
    frame4,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f2_canvas.place(x = 0, y = 0)

f2_background_img = PhotoImage(file = f"f4-background.png")
f2_background = f2_canvas.create_image(
    640.0, 522.5,
    image=f2_background_img)

label_symp= Label(frame4, text="", bg = "white")
label_symp.config(font=('Raleway', 16, 'bold'))
label_symp.place(x=255, y=307,
    width = 772,
    height = 258)

f2_img0 = PhotoImage(file = f"f4-img0.png")
f2_b0 = Button(frame4,
    image = f2_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_frame5,
    relief = "flat",
    activebackground = "#FFFFFF",
    cursor = 'hand2')
f2_b0.place(
    x = 944, y = 630,
    width = 157,
    height = 61)



f4_img1 = PhotoImage(file = f"f2-img1.png")
f4_b1 = Button(frame4,
    image = f2_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = toggle_win,
    relief = "flat",
    activebackground = "#1471C9",
    cursor = 'hand2')
f4_b1.place(
    x = 37, y = 13,
    width = 49,
    height = 34)


#-------------------FRAME5-------------------
f3_canvas = Canvas(
    frame5,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f3_canvas.place(x = 0, y = 0)

f3_background_img = PhotoImage(file = f"f5-background.png")
f3_background = f3_canvas.create_image(
    640.0, 517.5,
    image=f3_background_img)


#DISEASE PREDICTION: COMPLETE
label_frame= Label(frame5, bg = "white")
label_frame.place(x=263, y=310,
    width = 459,
    height = 50)
t3 = Text(label_frame, bd = 0)
t3.config(font=('Raleway', 28, 'bold'))
t3.pack(side= TOP, anchor="w")


#RECOMMENDATIONS: COMPLETE
label_frame1= Label(frame5, bg = "white")
label_frame1.place(x=252, y=429,
    width = 741,
    height = 145)
t4 = Text(label_frame1, bd = 0)
t4.config(font=('Raleway', 12))
t4.pack(side= TOP, anchor="w")


#CONFIDENCE RATING: INCOMPLETE
label_ac= Label(frame5, text="Very Likely", bg = "white")
label_ac.config(font=('Raleway', 16))
label_ac.place(x=765, y=316,
    width = 182,
    height = 44)



f5_img1 = PhotoImage(file = f"f2-img1.png")
f5_b1 = Button(frame5,
    image = f2_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = toggle_win,
    relief = "flat",
    activebackground = "#1471C9",
    cursor = 'hand2')
f5_b1.place(
    x = 37, y = 13,
    width = 49,
    height = 34)




window.resizable(False, False)
window.mainloop()
