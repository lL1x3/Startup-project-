from PyQt6 import QtCore, QtGui, QtWidgets
from testlayoutsecondwindow2 import *
from testlayoutthirdwindow2 import *
import sys
import json
import time
import random

with open('database1.json', 'r', encoding='utf-8') as fh:
    data = json.load(fh)
categorybrandlist=[]
categorylistforshow=["Молочные","Сладости","Рыба","Выпечка","Заморозка","Мясное","Овощи","Фрукты"]
indexlistplacment=[]
indexlist=[]
amountlist=[]
class Ui_MainApp(object):
    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.Form)
        self.FinForm = QtWidgets.QWidget()
        self.ui3 = Ui_FinalForm()
        self.ui3.setupUi(self.FinForm)
        for i in range(len(data["products"])):
            self.ui2.mainlistproducts.addItem(str(data["products"][i]["name"]+" "+data["products"][i]["brand"]+" "+data["products"][i]["price"]))
            indexlistplacment.append(i)
            if data["products"][i]["brand"] not in categorybrandlist:
                self.ui2.brandfilter.addItem(str(data["products"][i]["brand"]))
                categorybrandlist.append(str(data["products"][i]["brand"]))
        self.ui2.categoryfilter.addItems(categorylistforshow)
    def setupUi(self, MainApp):
        MainApp.setObjectName("MainApp")
        MainApp.resize(633, 863)
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(20)
        MainApp.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainApp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 590, 571, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.addproduct = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.addproduct.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setBold(True)
        font.setWeight(75)
        self.addproduct.setFont(font)
        self.addproduct.setObjectName("addproduct")
        self.gridLayout.addWidget(self.addproduct, 1, 0, 1, 1)
        self.toprice = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.toprice.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setBold(True)
        font.setWeight(75)
        self.toprice.setFont(font)
        self.toprice.setObjectName("toprice")
        self.gridLayout.addWidget(self.toprice, 3, 0, 1, 1)
        self.removeproduct = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.removeproduct.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setBold(True)
        font.setWeight(75)
        self.removeproduct.setFont(font)
        self.removeproduct.setObjectName("removeproduct")
        self.gridLayout.addWidget(self.removeproduct, 2, 0, 1, 1)
        self.iconright_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.iconright_2.setGeometry(QtCore.QRect(30, 10, 81, 71))
        self.iconright_2.setText("")
        self.iconright_2.setPixmap(QtGui.QPixmap("icon.png"))
        self.iconright_2.setScaledContents(True)
        self.iconright_2.setObjectName("iconright_2")
        self.WelcomeSignUnus = QtWidgets.QLabel(parent=self.centralwidget)
        self.WelcomeSignUnus.setGeometry(QtCore.QRect(110, 20, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomeSignUnus.setFont(font)
        self.WelcomeSignUnus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.WelcomeSignUnus.setObjectName("WelcomeSignUnus")
        self.iconright = QtWidgets.QLabel(parent=self.centralwidget)
        self.iconright.setGeometry(QtCore.QRect(520, 10, 81, 71))
        self.iconright.setText("")
        self.iconright.setPixmap(QtGui.QPixmap("icon.png"))
        self.iconright.setScaledContents(True)
        self.iconright.setObjectName("iconright")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 90, 571, 481))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        MainApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 26))
        self.menubar.setObjectName("menubar")
        self.toprice.setEnabled(False)
        self.addproduct.clicked.connect(self.openSecondWindow)
        MainApp.setMenuBar(self.menubar)
        self.ui2.addProducts.clicked.connect(self.closeSecondWindow)
        self.toprice.clicked.connect(self.openThirdWindow)
        self.ui3.pushButton_2.clicked.connect(self.closeThirdWindow)
        self.ui2.categoryfilter.activated.connect(self.categoryFiltering)
        self.ui2.brandfilter.activated.connect(self.categoryFiltering)
        self.ui2.addProducts.clicked.connect(self.addProductToMain)
        self.ui2.addProducts.clicked.connect(self.categoryFiltering)
        self.ui2.mainlistproducts.activated.connect(self.categoryFiltering)
        self.ui2.kidscheck.checkStateChanged.connect(self.filteringChecks)
        self.ui2.vegancheck.checkStateChanged.connect(self.filteringChecks)
        self.ui2.diabeticcheck.checkStateChanged.connect(self.filteringChecks)
        self.ui2.mainlistproducts.clicked.connect(self.enableAdd)
        self.ui2.mainlistproducts.activated.connect(self.enableAdd)
        self.removeproduct.clicked.connect(self.deleteProduct)
        self.toprice.clicked.connect(self.finalListCreator)
        self.ui3.pushButton_3.clicked.connect(self.finalWithoutCheck)
        self.ui3.pushButton.clicked.connect(self.finalWithCheck)
        self.removeproduct.pressed.connect(self.ChangeRemoveItem)


        self.retranslateUi(MainApp)
        QtCore.QMetaObject.connectSlotsByName(MainApp)
    def openSecondWindow(self):
        self.removeproduct.setEnabled(False)
        self.toprice.setEnabled(False)
        self.Form.show()
        self.ui2.addProducts.setEnabled(False)
    def closeSecondWindow(self):
        if self.ui2.mainlistproducts.currentRow()!=-1 and self.listWidget.count()!=-1:
            self.removeproduct.setEnabled(True)
            self.toprice.setEnabled(True)
        else: self.toprice.setEnabled(False)
        self.Form.close()
    def openThirdWindow(self):
        self.addproduct.setEnabled(False)
        self.removeproduct.setEnabled(False)
        self.FinForm.show()
    def closeThirdWindow(self):
        self.FinForm.close()
        self.addproduct.setEnabled(True)
        self.removeproduct.setEnabled(True)
    def enableAdd(self):
        if self.ui2.mainlistproducts.currentRow()!=-1:self.ui2.addProducts.setEnabled(True)
        else: self.ui2.addProducts.setEnabled(False)
    def ChangeRemoveItem(self):
        if self.listWidget.currentItem()!=None: self.removeproduct.setEnabled(True)
        elif self.listWidget.count()==-1:
            self.removeproduct.setEnabled(False)
            self.toprice.setEnabled(False)
    def FilterHelper(self,num):
        for i in range(len(data["products"])):
            if self.ui2.categoryfilter.currentIndex()==num and (data["products"][i]["category1"]==data["categories"][num-1] or data["products"][i]["category2"]==data["categories"][num-1]):
                if self.ui2.brandfilter.currentIndex()==0:
                    self.ui2.mainlistproducts.addItem(str(
                    data["products"][i]["name"] + " " + data["products"][i]["brand"] + " " + data["products"][i]["price"]))
                    indexlistplacment.append(i)
                elif categorybrandlist[self.ui2.brandfilter.currentIndex() - 1] == data["products"][i][
                    "brand"] and self.ui2.brandfilter.currentIndex() != 0:
                    self.ui2.mainlistproducts.addItem(str(
                        data["products"][i]["name"] + " " + data["products"][i]["brand"] + " " + data["products"][i][
                            "price"]))
                    indexlistplacment.append(i)
                else:
                    if categorybrandlist[self.ui2.brandfilter.currentIndex()-1]==data["products"][i]["brand"]:
                        self.ui2.mainlistproducts.addItem(str(data["products"][i]["name"] + " " + data["products"][i]["brand"] + " " + data["products"][i]["price"]))
                        indexlistplacment.append(i)
    def checkFilter(self,check):
        copycatlist=indexlistplacment.copy()
        if self.ui2.mainlistproducts.count()!=0:
            for i in range(self.ui2.mainlistproducts.count()):
                if self.ui2.mainlistproducts.item(i).isHidden()==False:
                    if data["products"][indexlistplacment[i]][check]=="Нет":
                        self.ui2.mainlistproducts.item(i).setHidden(True)
                        copycatlist.remove(indexlistplacment[i])
                    else:self.ui2.mainlistproducts.item(i).setHidden(False)
    def filteringChecks(self):
        if self.ui2.kidscheck.isChecked()==True or self.ui2.vegancheck.isChecked()==True or self.ui2.diabeticcheck.isChecked()==True:
            for i in range(self.ui2.mainlistproducts.count()):
                self.ui2.mainlistproducts.item(i).setHidden(False)
            if self.ui2.kidscheck.isChecked()==True: self.checkFilter("infantsfriendly")
            if self.ui2.vegancheck.isChecked()==True: self.checkFilter("veganfriendly")
            if self.ui2.diabeticcheck.isChecked()==True: self.checkFilter("diabeticfriendly")
        else:
            for i in range(self.ui2.mainlistproducts.count()):
                self.ui2.mainlistproducts.item(i).setHidden(False)

    def categoryFiltering(self):
        self.ui2.mainlistproducts.clear()
        indexlistplacment.clear()
        if self.ui2.categoryfilter.currentIndex()!=0 or self.ui2.brandfilter.currentIndex()!=0:
            if self.ui2.categoryfilter.currentIndex()==0:
                for i in range(len(data["products"])):
                    if categorybrandlist[self.ui2.brandfilter.currentIndex() - 1] == data["products"][i]["brand"] and self.ui2.brandfilter.currentIndex() != 0:
                        self.ui2.mainlistproducts.addItem(str(data["products"][i]["name"] + " " + data["products"][i]["brand"] + " " + data["products"][i][
                            "price"]))
                        indexlistplacment.append(i)
            else: self.FilterHelper(self.ui2.categoryfilter.currentIndex())
        elif self.ui2.categoryfilter.currentIndex()==0 and self.ui2.brandfilter.currentIndex()==0:
            for i in range(len(data["products"])):
                self.ui2.mainlistproducts.addItem(str(
                    data["products"][i]["name"] + " " + data["products"][i]["brand"] + " " + data["products"][i][
                        "price"]))
                indexlistplacment.append(i)
        else:
            for i in range(len(data["products"])):
                self.ui2.mainlistproducts.addItem(str(
                    data["products"][i]["name"] + " " + data["products"][i]["brand"] + " " + data["products"][i][
                        "price"]))
                indexlistplacment.append(i)
        self.filteringChecks()
    def addProductToMain(self):
        amount=self.ui2.addamountof.value()
        if indexlistplacment[self.ui2.mainlistproducts.currentRow()] in indexlist:
            sumamount=amountlist[indexlist.index(indexlistplacment[self.ui2.mainlistproducts.currentRow()])]+amount
            amountlist[indexlist.index(indexlistplacment[self.ui2.mainlistproducts.currentRow()])]=sumamount
            self.listWidget.item(indexlist.index(indexlistplacment[self.ui2.mainlistproducts.currentRow()])).setText((self.ui2.mainlistproducts.currentItem().text() + "x" +str(sumamount)))
        else:
            self.listWidget.addItem((self.ui2.mainlistproducts.currentItem().text()+"x"+str(amount)))
            indexlist.append(indexlistplacment[self.ui2.mainlistproducts.currentRow()])
            amountlist.append(amount)
        self.ui2.kidscheck.setChecked(False)
        self.ui2.vegancheck.setChecked(False)
        self.ui2.diabeticcheck.setChecked(False)
    def deleteProduct(self):
        if self.listWidget.count() != 0 and self.listWidget.currentItem()!=None:
            self.listWidget.takeItem(self.listWidget.row(self.listWidget.currentItem()))
            indexlist.pop(self.listWidget.row(self.listWidget.currentItem()))
            amountlist.pop(self.listWidget.row(self.listWidget.currentItem()))
        self.ChangeRemoveItem()

    def finalListCreator(self):
        self.ui3.puchaseditems.clear()
        if self.listWidget.count()==0:
            self.ui3.finalprice.setText('Товаров нет!')
            self.ui3.pushButton.setEnabled(False)
            self.ui3.pushButton_3.setEnabled(False)
        else:
            sum=0
            self.ui3.finalprice.setText('0')
            self.ui3.pushButton.setEnabled(True)
            self.ui3.pushButton_3.setEnabled(True)
            for i in range(self.listWidget.count()):
                self.ui3.puchaseditems.addItem(str(
                    data["products"][indexlist[i]]["name"] + " " + data["products"][indexlist[i]]["brand"] + " " + data["products"][indexlist[i]]["price"]+" x"+str(amountlist[i])))
                sum=sum+int(data["products"][indexlist[i]]["price"])*amountlist[i]
            self.ui3.finalprice.setText(str(sum)+" рублей")
    def finalEnabler(self,bl):
        self.ui3.pushButton.setEnabled(bl)
        self.ui3.pushButton_2.setEnabled(bl)
        self.ui3.pushButton_3.setEnabled(bl)
    def finalWithoutCheck(self):
        self.ui3.finalprice.setText("Подождите немного...")
        self.finalEnabler(False)
        time.sleep(2.5)
        self.ui3.finalprice.setText("Оплата прошла!")
        time.sleep(2.5)
        self.ui3.finalprice.setText('Оплачено!')
        self.finalEnabler(True)
        self.ui3.pushButton.setEnabled(False)
        self.ui3.pushButton_3.setEnabled(False)

    def finalWithCheck(self):
        sum=0
        timelocal = time.localtime()
        check_list = list("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
        check_list_final = str()
        for i in range(4): check_list_final = check_list_final + random.choice(check_list)
        check = open(("check" + str(random.randint(1000, 9999)) + check_list_final + ".txt"), "w+")
        for i in range(len(indexlist)):
            sum = sum + int(data["products"][indexlist[i]]["price"]) * amountlist[i]
            check.write(str(
                    data["products"][indexlist[i]]["name"] + " " + data["products"][indexlist[i]]["brand"] + " " + data["products"][indexlist[i]]["price"]+" x"+str(amountlist[i])+"\n"))
        check.write("Итоговая стоимость "+str(sum)+" руб. \n")
        check.write(time.strftime('%d.%m.%Y г. %H:%M:%S', timelocal))
        self.ui3.finalprice.setText("Подождите немного...")
        self.finalEnabler(False)
        time.sleep(2.5)
        self.ui3.finalprice.setText("Оплата прошла!")
        time.sleep(2.5)
        self.ui3.finalprice.setText('Оплачено! Чек отправлен')
        self.finalEnabler(True)
        self.ui3.pushButton.setEnabled(False)
        self.ui3.pushButton_3.setEnabled(False)


    def retranslateUi(self, MainApp):
        _translate = QtCore.QCoreApplication.translate
        MainApp.setWindowTitle(_translate("MainApp", "cashregister"))
        self.addproduct.setText(_translate("MainApp", "Добавить продукт"))
        self.toprice.setText(_translate("MainApp", "Рассчитать"))
        self.removeproduct.setText(_translate("MainApp", "Убрать выделенный продукт"))
        self.iconright_2.setText(_translate("MainApp", ""))
        self.WelcomeSignUnus.setText(_translate("MainApp", "Добро пожаловать!"))
        self.iconright.setText(_translate("MainApp", ""))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    cashregister = QtWidgets.QMainWindow()
    ui = Ui_MainApp()
    ui.setupUi(cashregister)
    cashregister.show()
    sys.exit(app.exec())