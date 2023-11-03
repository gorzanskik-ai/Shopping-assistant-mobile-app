from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

from help_str import help_str
import re
import pyrebase
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from collections import Counter
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDThemePicker
from datetime import date
import datetime

import cv2
import pytesseract
import numpy as np

import tkinter as tk
from tkinter import filedialog

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

root = tk.Tk()
root.withdraw()


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class ForgotPasswordScreen(Screen):
    pass


class ResetPassword(Screen):
    pass


class DeleteAccount(Screen):
    pass


class ListScreen(Screen):
    pass


class AddNewList(Screen):
    pass


class AddNewItemScreen(Screen):
    pass


class CalendarScreen(Screen):
    pass


class RenameListScreen(Screen):
    pass


class ShareListScreen(Screen):
    pass


class FriendsScreen(Screen):
    pass


class PickFriendScreen(Screen):
    pass


class TextRecognitionScreen(Screen):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()


class MainLists(MDCardSwipe):
    text = StringProperty()


class PopularItems(MDCardSwipe):
    text = StringProperty()


class FriendItemSwipe(MDCardSwipe):
    text = StringProperty()


class PickFriendItem(MDCardSwipe):
    text = StringProperty()


class CalendarWidget(MDCardSwipe):
    text = StringProperty()


class PickRecognizedItem(MDCard):
    text = StringProperty()

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(ForgotPasswordScreen(name="forgotpasswordscreen"))
sm.add_widget(ResetPassword(name="resetpassword"))
sm.add_widget(DeleteAccount(name="deleteaccount"))
sm.add_widget(AddNewList(name="addnewlist"))
sm.add_widget(ListScreen(name="listscreen"))
sm.add_widget(AddNewItemScreen(name="addnewitemscreen"))
sm.add_widget(CalendarScreen(name="calendarscreen"))
sm.add_widget(RenameListScreen(name="renamelistscreen"))
sm.add_widget(ShareListScreen(name="sharelistscreen"))
sm.add_widget(FriendsScreen(name="friendsscreen"))
sm.add_widget(PickFriendScreen(name="pickfriendscreen"))
sm.add_widget(TextRecognitionScreen(name="textrecognitionscreen"))


class ShoppingAssistantApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        firebaseConfig = {
            "apiKey":  "",
            "authDomain": "",
            "databaseURL": "",
            "storageBucket": ""

        }
        firebase = pyrebase.initialize_app(firebaseConfig)

        self.db = firebase.database()

        self.theme_cls.primary_palette = "Green"
        self.builder = Builder.load_string(help_str)
        self.email = ""
        self.mainWidgets = []
        self.listWidgets = []
        self.popularWidgets = []
        self.friendsWidgets = []
        self.pickFriendWidgets = []
        self.firstcalendarWidgets = []
        self.secondcalendarWidgets = []
        self.thirdcalendarWidgets = []
        self.fourthcalendarWidgets = []
        self.fifthcalendarWidgets = []
        self.checkedItems = []
        self.recognizedItmes = []
        self.recognizedItmesNames = []
        self.checkedRecognizedItems = []
        # self.url = "https://loginsetup-8f16a.firebaseio.com/.json"

    def build(self):
        return self.builder

    @staticmethod
    def email_validation(email):
        result = re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@"
                          r"([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]+$", email)
        return result

    @staticmethod
    def username_validation(username):
        result = re.match(r"^[A-Za-z0-9][A-Za-z0-9 ]*$", username)
        return result

    @staticmethod
    def password_validaiton(password):
        result = re.match(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])"
                          r"(?=.*[*!@$%^&(){}\[\]:;<>,\.?/~_+-=|]).{8,32}$", password)
        return result

    @staticmethod
    def name_of_list_validation(name):
        result = re.match(r"^[A-Za-z0-9][A-Za-z0-9 ]*$", name)
        return result

    @staticmethod
    def name_of_item_validation(name):
        result = re.match(r"^[A-Za-z0-9].[A-Za-z0-9 ]+$", name)
        return result

    def is_email_exist(self, user):
        users = self.db.child("Users").get()
        signupEmail = user.replace(".", "-")
        exist = False
        usersEach = users.each()  # gdy users.each() -> None, nie moza iterować
        if usersEach is not None:
            for user in usersEach:
                if user.key() == signupEmail:
                    exist = True
                    break
        return exist

    def is_friend_exist(self, friend):
        friends = self.db.child("Users").child(self.email).child("Friends").get()
        signupEmail = friend.replace(".", "-")
        exist = False
        friendsEach = friends.each()  # gdy users.each() -> None, nie moza iterować
        if friendsEach is not None:
            for user in friendsEach:
                if user.key() == signupEmail:
                    exist = True
                    break
        return exist

    def signup(self):
        signupEmail = self.builder.get_screen('signupscreen').ids.signup_email.text
        signupUsername = self.builder.get_screen('signupscreen').ids.signup_username.text
        signupPassword = self.builder.get_screen('signupscreen').ids.signup_password.text

        emailValidation = self.email_validation(signupEmail)
        usernameValidation = self.username_validation(signupUsername)
        passwordValidation = self.password_validaiton(signupPassword)

        exist = self.is_email_exist(signupEmail)

        if emailValidation and usernameValidation and passwordValidation and not exist:
            data = {
                'Username': signupUsername,
                'Password': signupPassword
            }
            signupEmail = signupEmail.replace(".", "-")
            self.db.child("Users").child(signupEmail).set(data)
            self.builder.get_screen('signupscreen').ids.signup_email.text = ""
            self.builder.get_screen('signupscreen').ids.signup_username.text = ""
            self.builder.get_screen('signupscreen').ids.signup_password.text = ""

            self.builder.get_screen('loginscreen').manager.current = 'loginscreen'

        elif exist:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)

            self.dialog = MDDialog(title='Invalid Input', text='This email adress is already used',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
            self.builder.get_screen('signupscreen').ids.signup_email.text = ""

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='Blank text fields are invalid \n\nPassword rules:\n-at least one digit'
                                        '\n-at least one lowercase character\n-at least one uppercase character\n'
                                        '-at least one special character\n'
                                        '-at least 8 characters in length, but no more than 32',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            if not emailValidation:
                self.builder.get_screen('signupscreen').ids.signup_email.text = ""
            if not usernameValidation:
                self.builder.get_screen('signupscreen').ids.signup_username.text = ""
            if not passwordValidation:
                self.builder.get_screen('signupscreen').ids.signup_password.text = ""

    def login(self):
        loginEmail = self.builder.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.builder.get_screen('loginscreen').ids.login_password.text

        exist = self.is_email_exist(loginEmail)
        emailValidation = self.email_validation(loginEmail)

        if emailValidation:
            loginEmail = loginEmail.replace(".", "-")
            correctPassword = self.db.child("Users").child(loginEmail).child("Password").get().val()
        else:
            correctPassword = ""

        passwordComparision = loginPassword == correctPassword

        if exist and passwordComparision:
            self.builder.get_screen('loginscreen').ids.login_email.text = ""
            self.builder.get_screen('loginscreen').ids.login_password.text = ""
            self.builder.get_screen('mainscreen').manager.current = 'mainscreen'
            self.email = loginEmail

            email = self.email
            email = email.replace('-', '.')
            self.builder.get_screen('mainscreen').ids.email.text = email

            self.builder.get_screen('mainscreen').ids.username.text = \
                self.db.child("Users").child(self.email).child("Username").get().val()

            self.show_lists()
            self.show_friends()

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='Blank text fields are invalid. Please enter a valid input',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            if not exist:
                self.builder.get_screen('loginscreen').ids.login_email.text = ""

            if not passwordComparision:
                self.builder.get_screen('loginscreen').ids.login_password.text = ""

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def logout_dialog(self):
        cancel_btn_dialogue = MDFlatButton(text='Cancel', on_release=self.close_username_dialog,
                                           text_color=self.theme_cls.primary_color)
        confirm_btn_dialogue = MDRaisedButton(text='Confirm', on_press=self.logout,
                                              text_color=self.theme_cls.primary_color)
        self.dialog = MDDialog(title='Confirmation',
                               text='Are you sure you want to logout? ',
                               size_hint=(0.7, 0.2),
                               buttons=[cancel_btn_dialogue, confirm_btn_dialogue])
        self.dialog.open()

    def logout(self, obj):
        self.builder.get_screen('loginscreen').manager.current = 'loginscreen'
        self.builder.get_screen('loginscreen').ids.login_email.text = ""
        self.builder.get_screen('loginscreen').ids.login_password.text = ""
        self.close_username_dialog(obj)
        self.builder.get_screen('mainscreen').ids.nav_drawer.set_state("close")
        self.remove_lists()
        self.remove_friends()

    def reset_password(self):
        email = self.builder.get_screen('resetpassword').ids.reset_email.text
        oldPassword = self.builder.get_screen('resetpassword').ids.reset_oldpassword.text
        newPassword = self.builder.get_screen('resetpassword').ids.reset_newpassword.text

        exist = self.is_email_exist(email)
        passwordValidation = self.password_validaiton(newPassword)
        emailValidation = self.email_validation(email)

        if emailValidation:
            email = email.replace(".", "-")
            correctPassword = self.db.child("Users").child(email).child("Password").get().val()
        else:
            correctPassword = ""

        passwordComparision = oldPassword == correctPassword

        if exist and passwordValidation and passwordComparision:
            self.db.child("Users").child(email).update({"Password": newPassword})

            self.builder.get_screen('loginscreen').manager.current = 'mainscreen'
            self.builder.get_screen('resetpassword').ids.reset_email.text = ""
            self.builder.get_screen('resetpassword').ids.reset_oldpassword.text = ""
            self.builder.get_screen('resetpassword').ids.reset_newpassword.text = ""

            cancel_btn_username_dialogue = MDRaisedButton(text='Ok', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='',
                                   text='Password has been changed',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='Blank text fields are invalid \n\nPassword rules:\n-at least one digit'
                                        '\n-at least one lowercase character\n-at least one uppercase character\n'
                                        '-at least one special character\n'
                                        '-at least 8 characters in length, but no more than 32',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            if not exist:
                self.builder.get_screen('resetpassword').ids.reset_email.text = ""
            if not passwordComparision:
                self.builder.get_screen('resetpassword').ids.reset_oldpassword.text = ""
            if not passwordValidation:
                self.builder.get_screen('resetpassword').ids.reset_newpassword.text = ""

    def forgot_password(self):
        email = self.builder.get_screen("forgotpasswordscreen").ids.reset_email.text
        email = email.replace('.', '-')

        data = self.db.child("Users").get().val()
        if data is not None:
            users = list(dict(data).keys())

            if email in users:
                password = self.db.child("Users").child(email).child("Password").get().val()
                message = Mail(from_email="",
                               to_emails="",
                               subject="",
                               plain_text_content="",
                               html_content=password)


                sg = SendGridAPIClient("")
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.header)


                cancel_btn_username_dialogue = MDRaisedButton(text='OK', on_release=self.close_username_dialog,
                                                              text_color=self.theme_cls.primary_color)
                self.dialog = MDDialog(title='',
                                       text='Email has send',
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

                self.builder.get_screen('loginscreen').manager.current = 'loginscreen'
                self.builder.get_screen('loginscreen').manager.transition.direction = 'right'
            else:
                cancel_btn_username_dialogue = MDRaisedButton(text='OK', on_release=self.close_username_dialog,
                                                              text_color=self.theme_cls.primary_color)
                self.dialog = MDDialog(title='',
                                       text='Email does not exist',
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='OK', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='',
                                   text='Email does not exist',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

        self.builder.get_screen("forgotpasswordscreen").ids.reset_email.text = ""

    def delete_account(self):
        email = self.builder.get_screen('deleteaccount').ids.delete_email.text
        password = self.builder.get_screen('deleteaccount').ids.delete_password.text

        exist = self.is_email_exist(email)
        emailValidaiton = self.email_validation(email)

        if emailValidaiton:
            email = email.replace(".", "-")
            passwordCorrect = self.db.child("Users").child(email).child("Password").get().val()
        else:
            passwordCorrect = ""

        passwordComparision = password == passwordCorrect

        if exist and passwordComparision:
            self.db.child("Users").child(email).remove()

            cancel_btn_username_dialogue = MDRaisedButton(text='OK', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='',
                                   text='Account has succesfully removed',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            self.builder.get_screen('deleteaccount').ids.delete_email.text = ""
            self.builder.get_screen('deleteaccount').ids.delete_password.text = ""
            self.builder.get_screen('mainscreen').ids.nav_drawer.set_state("close")
            self.builder.get_screen('loginscreen').manager.current = 'loginscreen'

            data = self.db.child("Users").get().val()
            if data is not None:
                users = list(dict(data).keys())

                for user in users:
                    self.db.child("Users").child(user).child("Friends").child(email).remove()

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='Blank text fields are invalid. Pleasse enter valid input',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            if not exist:
                self.builder.get_screen('deleteaccount').ids.delete_email.text = ""
            if not passwordComparision:
                self.builder.get_screen('deleteaccount').ids.delete_password.text = ""

    def remove_item(self, instance):
        self.builder.get_screen('listscreen').ids.items_list.remove_widget(instance)
        name_of_list = self.builder.get_screen('listscreen').ids.created_list.title
        self.db.child("Users").child(self.email).child("Lists").child(name_of_list).child(instance.id).remove()

    def item_added_to_basket(self, instance):
        currentColor = instance.ids.item_added_color.md_bg_color

        if currentColor == [1.0, 1.0, 1.0, 1]:
            instance.ids.item_added_color.md_bg_color = [0.65, 0.65, 0.65, 1]  # [158/255, 102/255, 46/255, 1.0]
            self.checkedItems.append(instance)
        else:
            instance.ids.item_added_color.md_bg_color = [1.0, 1.0, 1.0, 1]
            self.checkedItems.remove(instance)

    def remove_checked_items(self):
        if len(self.checkedItems) == 0:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='No one item is checked',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            name_of_list = self.builder.get_screen('listscreen').ids.created_list.title
            for i in self.checkedItems:
                self.builder.get_screen('listscreen').ids.items_list.remove_widget(i)
                self.db.child("Users").child(self.email).child("Lists").child(name_of_list).child(i.id).remove()

            self.checkedItems.clear()

    def remove_lists(self):
        for i in self.mainWidgets:
            self.builder.get_screen('mainscreen').ids.md_list2.remove_widget(i)

    def remove_items(self):
        for i in self.listWidgets:
            self.builder.get_screen('listscreen').ids.items_list.remove_widget(i)

    def delete_list_dialog(self):
        cancel_btn_dialogue = MDFlatButton(text='Cancel', on_release=self.close_username_dialog,
                                           text_color=self.theme_cls.primary_color)
        confirm_btn_dialogue = MDRaisedButton(text='Confirm', on_press=self.delete_list,
                                              text_color=self.theme_cls.primary_color)
        self.dialog = MDDialog(title='Confirmation',
                               text='Are you sure you want to delete list? ',
                               size_hint=(0.7, 0.2),
                               buttons=[cancel_btn_dialogue, confirm_btn_dialogue])
        self.dialog.open()

    def delete_list(self, obj):
        name_of_list = self.builder.get_screen('listscreen').ids.created_list.title
        self.db.child("Users").child(self.email).child("Lists").child(name_of_list).remove()
        self.remove_lists()
        self.show_lists()
        self.remove_items()
        self.builder.get_screen("mainscreen").manager.current = "mainscreen"
        self.builder.get_screen('mainscreen').manager.transition.direction = 'right'
        self.close_username_dialog(obj)

        data = self.db.child("Users").child(self.email).child("Calendar").get().val()
        if data is not None:
            days = list(dict(data).keys())

            for day in days:
                self.db.child("Users").child(self.email).child("Calendar").child(day).child(name_of_list).remove()

    def show_lists(self):
        data = self.db.child("Users").child(self.email).child("Lists").get()
        lists = []
        dataEach = data.each()
        if dataEach is not None:
            for i in dataEach:
                lists.append(i.key())

            for i in lists:
                newWidget = MainLists(text=str(i), id=str(i))
                self.mainWidgets.append(newWidget)
                self.builder.get_screen('mainscreen').ids.md_list2.add_widget(newWidget)

    def refresh_lists(self):
        self.remove_lists()
        self.show_lists()

    def create_new_list(self):
        nameOfList = self.builder.get_screen('addnewlist').ids.new_list_name.text

        nameOfListValidation = self.name_of_list_validation(nameOfList)

        if nameOfListValidation:
            data = self.db.child("Users").child(self.email).child("Lists").get()
            lists = []
            dataEach = data.each()
            if dataEach is not None:
                for i in dataEach:
                    lists.append(i.key())
            exist = nameOfList in lists

        else:
            exist = False

        if not exist and nameOfListValidation:
            self.db.child("Users").child(self.email).child("Lists").child(nameOfList).set(["x"])
            self.builder.get_screen('addnewlist').ids.new_list_name.text = ""
            newWidget = MainLists(text=nameOfList, id=nameOfList)
            self.mainWidgets.append(newWidget)
            self.builder.get_screen('mainscreen').ids.md_list2.add_widget(newWidget)
            self.builder.get_screen('listscreen').ids.created_list.title = nameOfList
            self.builder.get_screen('addnewitemscreen').ids.adding_items_toolbar.title = nameOfList
            self.builder.get_screen('listscreen').manager.current = 'listscreen'
            self.builder.get_screen('listscreen').manager.transition.direction = 'left'

        elif exist or not nameOfListValidation:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='List already exist or name of list can not contains special characters',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            self.builder.get_screen('addnewlist').ids.new_list_name.text = ""

    def back_to_main(self):
        self.builder.get_screen('mainscreen').manager.current = 'mainscreen'
        self.builder.get_screen('mainscreen').manager.transition.direction = 'right'
        self.remove_items()
        self.checkedItems.clear()

    def back_to_login(self):
        self.builder.get_screen('loginscreen').manager.current = 'loginscreen'
        self.builder.get_screen('loginscreen').manager.transition.direction = 'right'
        self.builder.get_screen('forgotpasswordscreen').ids.reset_email.text = ""

    def back_to_main_from_friends(self):
        self.builder.get_screen('mainscreen').manager.current = 'mainscreen'
        self.builder.get_screen('mainscreen').manager.transition.direction = 'left'

    def back_to_list(self):
        self.builder.get_screen('listscreen').manager.current = 'listscreen'
        self.builder.get_screen('listscreen').manager.transition.direction = 'right'
        self.builder.get_screen('addnewitemscreen').ids.add_new_item.text = ""
        self.delete_popular_items()

    def go_to_sharelistscreen(self):
        self.builder.get_screen('sharelistscreen').manager.current = 'sharelistscreen'
        self.builder.get_screen('sharelistscreen').manager.transition.direction = 'left'

    def back_to_pickfriendscreen(self):
        self.builder.get_screen('pickfriendscreen').manager.current = 'pickfriendscreen'
        self.builder.get_screen('pickfriendscreen').manager.transition.direction = 'right'
        self.builder.get_screen("sharelistscreen").ids.share_list_user.text = ""

    def back_to_list_from_calendar(self):
        self.builder.get_screen('mainscreen').manager.current = 'mainscreen'
        self.builder.get_screen('mainscreen').manager.transition.direction = 'left'
        self.remove_calendar()

    def open_list(self, instance):
        self.builder.get_screen('listscreen').manager.current = 'listscreen'
        self.builder.get_screen('listscreen').manager.transition.direction = 'left'
        self.builder.get_screen('listscreen').ids.created_list.title = instance.text
        self.builder.get_screen('addnewitemscreen').ids.adding_items_toolbar.title = instance.text

        data = self.db.child("Users").child(self.email).child("Lists").child(instance.text).get()
        length = len(data.val())

        if length > 1:
            dictionary = dict(data.val())
            dictionary.pop('0')
            items = list(dictionary.keys())

            for i in items:
                newWidget = SwipeToDeleteItem(text=i, id=i)
                self.listWidgets.append(newWidget)
                self.builder.get_screen('listscreen').ids.items_list.add_widget(newWidget)

        self.builder.get_screen('mainscreen').ids.nav_drawer.set_state("close")

    def add_new_item(self):
        item = self.builder.get_screen('addnewitemscreen').ids.add_new_item.text
        name_of_list = self.builder.get_screen('listscreen').ids.created_list.title

        itemValidation = self.name_of_item_validation(item)

        if not item == "" and itemValidation:
            data = self.db.child("Users").child(self.email).child("Lists").child(name_of_list).get()
            items = []
            if data.each is not None:
                for i in data.each():
                    items.append(i.key())

            exist = item in items
            if not exist:
                newWidget = SwipeToDeleteItem(text=item, id=item)
                self.listWidgets.append(newWidget)
                self.builder.get_screen('listscreen').ids.items_list.add_widget(newWidget)

                self.db.child("Users").child(self.email).child("Lists").child(name_of_list).child(item).set(["x"])

                self.builder.get_screen('addnewitemscreen').ids.add_new_item.text = ""

                self.delete_popular_items()
                self.popular_items()

            else:
                cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                              text_color=self.theme_cls.primary_color)
                self.dialog = MDDialog(title='Invalid Input',
                                       text='Item already exist at list',
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
                self.builder.get_screen('addnewitemscreen').ids.add_new_item.text = ""

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='Name of item must consist of at least one character and can not consist of '
                                        'special characetrs',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            self.builder.get_screen('addnewitemscreen').ids.add_new_item.text = ""

    def popular_items(self):
        all_items = []

        data = self.db.child("Users").get()
        users = []
        if data.each is not None:
            for i in data.each():
                users.append(i.key())

        for user in users:
            data = self.db.child("Users").child(user).child("Lists").get().val()

            if data is not None:
                lists = list(dict(data))

                for i in lists:
                    data = self.db.child("Users").child(user).child("Lists").child(i).get()
                    if data.each is not None:
                        for item in data.each():
                            all_items.append(item.key())

        for i in range(all_items.count('0')):
            all_items.remove('0')
        for i in range(all_items.count(0)):
            all_items.remove(0)

        keys = list(Counter(all_items).keys())
        values = list(Counter(all_items).values())

        dictionary = {}
        for k, v in zip(keys, values):
            dictionary[k] = v

        sortItems = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
        most_popular = list(sortItems.keys())

        name_of_list = self.builder.get_screen('listscreen').ids.created_list.title
        data = self.db.child("Users").child(self.email).child("Lists").child(name_of_list).get().val()

        if data is not None:
            if len(data) > 1:
                currentItems = list(dict(data))
                currentItems.remove('0')

                for i in currentItems:
                    most_popular.remove(i)

        #print(most_popular)

        for i in most_popular:
            newWidget = PopularItems(text=i, id=i)
            self.popularWidgets.append(newWidget)
            self.builder.get_screen('addnewitemscreen').ids.popular_items.add_widget(newWidget)

    def delete_popular_items(self):
        for i in self.popularWidgets:
            self.builder.get_screen('addnewitemscreen').ids.popular_items.remove_widget(i)

    def add_popular_item(self, instance):
        item = instance.id
        name_of_list = self.builder.get_screen('listscreen').ids.created_list.title

        data = self.db.child("Users").child(self.email).child("Lists").child(name_of_list).get()
        items = []
        if data.each is not None:
            for i in data.each():
                items.append(i.key())

        exist = item in items

        if not exist:
            newWidget = SwipeToDeleteItem(text=item, id=item)
            self.listWidgets.append(newWidget)
            self.builder.get_screen('listscreen').ids.items_list.add_widget(newWidget)
            self.db.child("Users").child(self.email).child("Lists").child(name_of_list).child(item).set(["x"])

            self.delete_popular_items()
            self.popular_items()

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='Item already exist at list',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

    def rename_list(self):
        nameOfList = self.builder.get_screen("renamelistscreen").ids.new_list_name.text
        currentList = self.builder.get_screen("listscreen").ids.created_list.title
        nameOfListValidation = self.name_of_list_validation(nameOfList)

        if nameOfListValidation:
            data = self.db.child("Users").child(self.email).child("Lists").get()
            lists = []
            dataEach = data.each()
            if dataEach is not None:
                for i in dataEach:
                    lists.append(i.key())
            exist = nameOfList in lists
        else:
            exist = False

        if not exist and nameOfListValidation:
            data = self.db.child("Users").child(self.email).child("Lists").child(currentList).get()
            items = []
            if len(data.val()) > 1:
                dataEach = data.each()
                if dataEach is not None:
                    for i in dataEach:
                        items.append(i.key())
            items.remove('0')

            self.remove_items()

            self.db.child("Users").child(self.email).child("Lists").child(nameOfList).set(["x"])
            for item in items:
                self.db.child("Users").child(self.email).child("Lists").child(nameOfList).child(item).set(["x"])
                newWidget = SwipeToDeleteItem(text=item, id=item)
                self.listWidgets.append(newWidget)
                self.builder.get_screen('listscreen').ids.items_list.add_widget(newWidget)
            self.remove_lists()

            data = self.db.child("Users").child(self.email).child("Calendar").get().val()
            if data is not None:
                days = list(dict(data))

                for day in days:
                    data = self.db.child("Users").child(self.email).child("Calendar").child(day).get().val()
                    lists = list(dict(data))

                    if currentList in lists:
                        self.db.child("Users").child(self.email).child("Calendar").child(day).child(currentList).remove()
                        self.db.child("Users").child(self.email).child("Calendar").child(day).child(nameOfList).set(['x'])

            self.builder.get_screen("listscreen").ids.created_list.title = nameOfList
            self.db.child("Users").child(self.email).child("Lists").child(currentList).remove()
            self.show_lists()
            self.builder.get_screen("listscreen").manager.current = 'listscreen'
            self.builder.get_screen("listscreen").manager.transition.direction = 'up'
            self.builder.get_screen("renamelistscreen").ids.new_list_name.text = ""

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='List already exist or name of list can not contains special characetrs',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

    def share_list(self):
        friendEmail = self.builder.get_screen("sharelistscreen").ids.share_list_user.text
        username = self.db.child("Users").child(self.email).child("Username").get().val()
        emailValidation = self.email_validation(friendEmail)
        exist = self.is_email_exist(friendEmail)
        friendEmail = friendEmail.replace('.', '-')
        listShare = self.builder.get_screen("listscreen").ids.created_list.title
        nameOfListToShare = self.builder.get_screen("sharelistscreen").ids.custom_list.text + " from " + username
        nameOfListValidation = self.name_of_list_validation(nameOfListToShare)

        if exist and emailValidation and not (friendEmail == self.email) and nameOfListValidation:

            data = self.db.child("Users").child(self.email).child("Lists").child(listShare).get()
            items = []
            if len(data.val()) > 1:
                dataEach = data.each()
                if dataEach is not None:
                    for i in dataEach:
                        items.append(i.key())
            items.remove('0')

            lists_of_friend = self.db.child("Users").child(friendEmail).child("Lists").get()
            listExist = False
            listsEach = lists_of_friend.each()  # gdy users.each() -> None, nie moza iterować
            if listsEach is not None:
                for user in listsEach:
                    if user.key() == nameOfListToShare:
                        listExist = True
                        break

            if not listExist:
                self.db.child("Users").child(friendEmail).child("Lists").child(nameOfListToShare).set(["x"])
                for item in items:
                    self.db.child("Users").child(friendEmail).child("Lists"). \
                        child(nameOfListToShare).child(item).set(["x"])

                self.builder.get_screen("listscreen").manager.current = "listscreen"
                self.builder.get_screen('mainscreen').manager.transition.direction = 'down'
                self.builder.get_screen("sharelistscreen").ids.share_list_user.text = ""
                self.remove_friends_to_pick()

            else:
                cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                              text_color=self.theme_cls.primary_color)
                self.dialog = MDDialog(title='Invalid Input',
                                       text="Name of list exist in friend's lists",
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

            #self.builder.get_screen("sharelistscreen").ids.share_list_user.text = ""
            self.builder.get_screen("sharelistscreen").ids.custom_list.text = ""

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='Email does not exist or is invalid or or belongs to you or '
                                        'name of list contains special characters'
                                        '. Blank text fields are invalid',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            if not exist or not emailValidation or (friendEmail == self.email):
                self.builder.get_screen("sharelistscreen").ids.share_list_user.text = ""
            if not nameOfListValidation:
                self.builder.get_screen("sharelistscreen").ids.custom_list.text = ""

    def add_new_friend(self):
        newFriendEmail = self.builder.get_screen("friendsscreen").ids.add_new_friend.text
        emailValidation = self.email_validation(newFriendEmail)
        newFriendEmail = newFriendEmail.replace('.', '-')
        existEmail = self.is_email_exist(newFriendEmail)

        if existEmail and emailValidation and not (newFriendEmail == self.email):
            existFriend = self.is_friend_exist(newFriendEmail)

            if not existFriend:
                self.db.child("Users").child(self.email).child("Friends").child(newFriendEmail).set(["x"])
                newFriendEmail = newFriendEmail.replace('-', '.')

                newWidget = FriendItemSwipe(text=newFriendEmail, id=newFriendEmail)
                self.friendsWidgets.append(newWidget)
                self.builder.get_screen('friendsscreen').ids.friends_list.add_widget(newWidget)

                self.builder.get_screen("friendsscreen").ids.add_new_friend.text = ""

            else:
                cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                              text_color=self.theme_cls.primary_color)
                self.dialog = MDDialog(title='Invalid Input',
                                       text='This email belongs to your firend already',
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()

                self.builder.get_screen("friendsscreen").ids.add_new_friend.text = ""

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='Email does not exist or is invalid or belongs to you',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

            self.builder.get_screen("friendsscreen").ids.add_new_friend.text = ""

    def show_friends(self):
        data = self.db.child("Users").child(self.email).child("Friends").get()
        friends = []
        friendsEach = data.each()
        if friendsEach is not None:
            for i in friendsEach:
                friends.append(i.key())

            for i in friends:
                i = i.replace('-', '.')
                newWidget = FriendItemSwipe(text=str(i), id=str(i))
                self.friendsWidgets.append(newWidget)
                self.builder.get_screen('friendsscreen').ids.friends_list.add_widget(newWidget)

    def remove_friends(self):
        for i in self.friendsWidgets:
            self.builder.get_screen('friendsscreen').ids.friends_list.remove_widget(i)

    def remove_friend(self, instance):
        friend = instance.id
        self.builder.get_screen('friendsscreen').ids.friends_list.remove_widget(instance)
        friend = friend.replace('.', '-')
        self.db.child("Users").child(self.email).child("Friends").child(friend).remove()

    def show_friends_to_pick(self):
        data = self.db.child("Users").child(self.email).child("Friends").get()
        friends = []
        friendsEach = data.each()
        if friendsEach is not None:
            for i in friendsEach:
                friends.append(i.key())

            for i in friends:
                i = i.replace('-', '.')
                newWidget = PickFriendItem(text=str(i), id=str(i))
                self.pickFriendWidgets.append(newWidget)
                self.builder.get_screen('pickfriendscreen').ids.pick_friend_list.add_widget(newWidget)

    def remove_friends_to_pick(self):
        for i in self.pickFriendWidgets:
            self.builder.get_screen('pickfriendscreen').ids.pick_friend_list.remove_widget(i)

    def pick_a_friend(self, instance):
        friend = instance.id
        self.builder.get_screen("sharelistscreen").ids.share_list_user.text = friend
        self.builder.get_screen('listscreen').manager.current = 'sharelistscreen'
        self.builder.get_screen('listscreen').manager.transition.direction = 'left'

    def set_date(self):
        picker = MDDatePicker(callback=self.get_date)
        picker.open()

    def get_date(self, the_date):
        listName = self.builder.get_screen("listscreen").ids.created_list.title
        self.db.child("Users").child(self.email).child("Calendar").child(the_date).child(listName).set(["x"])

    @staticmethod
    def show_themepicker():
        picker = MDThemePicker()
        picker.open()

    def show_calendar(self):
        today = date.today()
        todayString = str(date.today())

        oneWeek = [todayString]
        self.builder.get_screen("calendarscreen").ids.first_day_label.text = todayString

        second_day = today + datetime.timedelta(days=1)
        oneWeek.append((str(second_day)))
        self.builder.get_screen("calendarscreen").ids.second_day_label.text = str(second_day)

        third_day = today + datetime.timedelta(days=2)
        oneWeek.append((str(third_day)))
        self.builder.get_screen("calendarscreen").ids.third_day_label.text = str(third_day)

        fourth_day = today + datetime.timedelta(days=3)
        oneWeek.append((str(fourth_day)))
        self.builder.get_screen("calendarscreen").ids.fourth_day_label.text = str(fourth_day)

        fifth_day = today + datetime.timedelta(days=4)
        oneWeek.append((str(fifth_day)))
        self.builder.get_screen("calendarscreen").ids.fifth_day_label.text = str(fifth_day)

        data = self.db.child("Users").child(self.email).child("Calendar").get().val()
        if data is not None:
            days = list(dict(data).keys())
            daysHaveGone = []

            for day in days:
                if day < todayString:
                    daysHaveGone.append(day)

            for day in daysHaveGone:
                self.db.child("Users").child(self.email).child("Calendar").child(day).remove()

            # commonParts = list(set(days).intersection(oneWeek))

            data = self.db.child("Users").child(self.email).child("Calendar").child(oneWeek[0]).get().val()
            if data is not None:
                lists = list(dict(data))
                for l in lists:
                    newWidget = CalendarWidget(text=l, id=oneWeek[0])
                    self.firstcalendarWidgets.append(newWidget)
                    self.builder.get_screen('calendarscreen').ids.first_day_list.add_widget(newWidget)

            data = self.db.child("Users").child(self.email).child("Calendar").child(oneWeek[1]).get().val()
            if data is not None:
                lists = list(dict(data))
                for l in lists:
                    newWidget = CalendarWidget(text=l, id=oneWeek[1])
                    self.secondcalendarWidgets.append(newWidget)
                    self.builder.get_screen('calendarscreen').ids.second_day_list.add_widget(newWidget)

            data = self.db.child("Users").child(self.email).child("Calendar").child(oneWeek[2]).get().val()
            if data is not None:
                lists = list(dict(data))
                for l in lists:
                    newWidget = CalendarWidget(text=l, id=oneWeek[2])
                    self.thirdcalendarWidgets.append(newWidget)
                    self.builder.get_screen('calendarscreen').ids.third_day_list.add_widget(newWidget)

            data = self.db.child("Users").child(self.email).child("Calendar").child(oneWeek[3]).get().val()
            if data is not None:
                lists = list(dict(data))
                for l in lists:
                    newWidget = CalendarWidget(text=l, id=oneWeek[3])
                    self.fourthcalendarWidgets.append(newWidget)
                    self.builder.get_screen('calendarscreen').ids.fourth_day_list.add_widget(newWidget)

            data = self.db.child("Users").child(self.email).child("Calendar").child(oneWeek[4]).get().val()
            if data is not None:
                lists = list(dict(data))
                for l in lists:
                    newWidget = CalendarWidget(text=l, id=oneWeek[4])
                    self.fifthcalendarWidgets.append(newWidget)
                    self.builder.get_screen('calendarscreen').ids.fifth_day_list.add_widget(newWidget)

    def remove_calendar(self):
        for i in self.firstcalendarWidgets:
            self.builder.get_screen('calendarscreen').ids.first_day_list.remove_widget(i)
        for i in self.secondcalendarWidgets:
            self.builder.get_screen('calendarscreen').ids.second_day_list.remove_widget(i)
        for i in self.thirdcalendarWidgets:
            self.builder.get_screen('calendarscreen').ids.third_day_list.remove_widget(i)
        for i in self.fourthcalendarWidgets:
            self.builder.get_screen('calendarscreen').ids.fourth_day_list.remove_widget(i)
        for i in self.fifthcalendarWidgets:
            self.builder.get_screen('calendarscreen').ids.fifth_day_list.remove_widget(i)

    def remove_calendar_widget(self, instance):
        self.remove_calendar()
        dateOfShopping = instance.id
        nameOfList = instance.text
        self.db.child("Users").child(self.email).child("Calendar").child(dateOfShopping).child(nameOfList).remove()
        self.show_calendar()

    def recognize_photo(self):
        file_path = filedialog.askopenfilename()
        file_extensions = ['jpg', 'jpeg', 'png', 'JPEG', 'JPG', 'PNG']
        tmp = file_path.split('.')
        file_extension = tmp[-1]

        if bool(file_path) and file_extension in file_extensions:
            file_path = file_path.replace('/', '\\')
            img = cv2.imread(file_path)

            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            gray, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            gray = cv2.bitwise_not(img_bin)

            kernel = np.ones((2, 1), np.uint8)
            img = cv2.erode(gray, kernel, iterations=1)
            img = cv2.dilate(img, kernel, iterations=1)
            out_below = pytesseract.image_to_string(img)
            productsImage = out_below.split("\n")
            productsImage.remove('\x0c')

            for i in range(len(productsImage)):
                productsImage[i] = productsImage[i].lower()

            name_of_list = self.builder.get_screen('listscreen').ids.created_list.title
            data = self.db.child("Users").child(self.email).child("Lists").child(name_of_list).get().val()

            newProducts = []
            if data is not None:
                if len(data) > 1:
                    products = list(dict(data))
                    products.remove('0')
                else:
                    products = []

                for product in productsImage:
                    if product not in products:
                        newProducts.append(product)

                if len(newProducts) == 0:
                    cancel_btn_username_dialogue = MDRaisedButton(text='Ok', on_release=self.close_username_dialog,
                                                                  text_color=self.theme_cls.primary_color)
                    self.dialog = MDDialog(title='',
                                           text='All items already exist at list',
                                           size_hint=(0.7, 0.2),
                                           buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()

                else:
                    for i in newProducts:
                        if i not in self.recognizedItmesNames:
                            newWidget = PickRecognizedItem(text=i, id=i)
                            self.recognizedItmes.append(newWidget)
                            self.builder.get_screen('textrecognitionscreen').ids.recognized_items.add_widget(newWidget)
                            #self.db.child("Users").child(self.email).child("Lists").child(name_of_list).child(i).set(['x'])
                            self.recognizedItmesNames.append(i)

            '''
            else:
                newProducts = productsImage
                for i in newProducts:
                    newWidget = PickRecognizedItem(text=i, id=i)
                    self.recognizedItmes.append(newWidget)
                    self.builder.get_screen('textrecognitionscreen').ids.recognized_items.add_widget(newWidget)
                    #self.db.child("Users").child(self.email).child("Lists").child(name_of_list).child(i).set(['x'])
            '''

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid input',
                                   text='You picked no path or path is invalid',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

    def go_to_recognition_screen(self):
        self.builder.get_screen('textrecognitionscreen').manager.current = 'textrecognitionscreen'
        self.builder.get_screen('textrecognitionscreen').manager.transition.direction = 'down'
        self.remove_recognized_items()
        self.recognizedItmesNames.clear()
        self.recognizedItmes.clear()

    def remove_recognized_item(self, instance):
        self.builder.get_screen('textrecognitionscreen').ids.recognized_items.remove_widget(instance)
        self.recognizedItmes.remove(instance)
        self.recognizedItmesNames.remove(instance.id)

    def remove_recognized_items(self):
        for i in self.recognizedItmes:
            self.builder.get_screen('textrecognitionscreen').ids.recognized_items.remove_widget(i)

    def add_recognized_items(self):
        name_of_list = self.builder.get_screen('listscreen').ids.created_list.title
        if len(self.recognizedItmes) > 0:
            for i in self.recognizedItmes:
                newWidget = SwipeToDeleteItem(text=i.id, id=i.id)
                self.listWidgets.append(newWidget)
                self.builder.get_screen('listscreen').ids.items_list.add_widget(newWidget)

                self.db.child("Users").child(self.email).child("Lists").child(name_of_list).child(i.id).set(['x'])

            self.builder.get_screen('listscreen').manager.current = 'listscreen'
            self.builder.get_screen('listscreen').manager.transition.direction = 'up'

            self.recognizedItmesNames.clear()
            self.remove_recognized_items()
            self.recognizedItmes.clear()

        else:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='There is no items to add',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()



    def check_recognized_item(self, instance):
        currentColor = instance.ids.item_added_color_2.md_bg_color

        if currentColor == [1.0, 1.0, 1.0, 1]:
            instance.ids.item_added_color_2.md_bg_color = [0.65, 0.65, 0.65, 1]  # [158/255, 102/255, 46/255, 1.0]
            self.checkedRecognizedItems.append(instance)
        else:
            instance.ids.item_added_color_2.md_bg_color = [1.0, 1.0, 1.0, 1]
            self.checkedRecognizedItems.remove(instance)

    def remove_checked_recognized_items(self):
        if len(self.checkedRecognizedItems) == 0:
            cancel_btn_username_dialogue = MDRaisedButton(text='Retry', on_release=self.close_username_dialog,
                                                          text_color=self.theme_cls.primary_color)
            self.dialog = MDDialog(title='Invalid Input',
                                   text='No one item is checked',
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            for i in self.checkedRecognizedItems:
                self.builder.get_screen('textrecognitionscreen').ids.recognized_items.remove_widget(i)
                self.recognizedItmes.remove(i)
                self.recognizedItmesNames.remove(i.id)
                #self.db.child("Users").child(self.email).child("Lists").child(name_of_list).child(i.id).remove()

            self.checkedRecognizedItems.clear()


ShoppingAssistantApp().run()
