help_str = '''

ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    ForgotPasswordScreen:
    ResetPassword:
    DeleteAccount:
    AddNewList:
    ListScreen:
    AddNewItemScreen:
    CalendarScreen:
    RenameListScreen:
    ShareListScreen:
    FriendsScreen:
    PickFriendScreen:
    TextRecognitionScreen:

<WelcomeScreen>:
    name:'welcomescreen'

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        Image:
            source: "logo.png"
            #size: self.texture_size
            pos_hint: {'center_y':0.8}

        MDLabel:
            text:"Nice to see you"
            font_style:'H4'
            halign:'center'
            pos_hint: {'center_y':0.6}
        MDLabel:
            text:"Let's get started"
            font_style:'H4'
            halign:'center'
            pos_hint: {'center_y':0.4}
        MDFillRoundFlatButton:
            text:'Sign In'
            pos_hint : {'center_x':0.5,'center_y':0.3}
            size_hint_x: 0.8
            font_size: 20
            on_press: 
                root.manager.current = 'loginscreen'
                root.manager.transition.direction = 'left'
        MDFillRoundFlatButton:
            text:'Sign Up'
            pos_hint : {'center_x':0.5,'center_y':0.2}
            size_hint_x: 0.8
            font_size: 20
            on_press:
                root.manager.current = 'signupscreen'
                root.manager.transition.direction = 'left'


<LoginScreen>:
    name:'loginscreen'

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        MDCard:
            #size_hint: 0.9, None
            #size_hint_x: 0.8
            #size_hint_y: 0.8
            size_hint: None, None
            size: 320, 460
            pos_hint:   {"center_x": 0.5, "center_y": 0.5}
            elevation: 15
            #md_bg_color: [151/255, 218/255, 250/255, 1]
            padding: 20
            spacing: 30
            orientation: "vertical"

            MDLabel:
                text:'Sign In'
                halign:'center'
                font_size: 45
                size_hint_y:  None
                #size_hint_x: .8
                height: self.texture_size[1]
                padding_y: 15
            MDTextField:
                id:login_email
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: 220
                #size_hint_x: .8
                font_size: 20
                hint_text: 'Email'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'account'
                icon_right_color: app.theme_cls.primary_color
                required: True
            MDTextField:
                id:login_password
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                #size_hint_x: .8
                font_size: 20
                hint_text: 'Password'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'key-variant'
                icon_right_color: app.theme_cls.primary_color
                required: True
                password: True
            MDTextButton:
                text: "Forgot password?"
                pos_hint: {"center_x": 0.5}
                font_size: 15
                on_press:
                    root.manager.current = 'forgotpasswordscreen'
                    root.manager.transition.direction = 'left'
            MDFillRoundFlatButton:
                text:'LOGIN'
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                font_size: 20
                on_press:
                    app.login()
                    root.manager.transition.direction = 'down'
                    #app.username_changer()
            MDRoundFlatButton:
                text: "Create an account"
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press:
                    root.manager.current = 'signupscreen'
                    root.manager.transition.direction = 'up'

<SignupScreen>:
    name:'signupscreen'

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        MDCard:
            size_hint: None, None
            size: 320, 500
            pos_hint:   {"center_x": 0.5, "center_y": 0.5}
            elevation: 15
            md_bg_color: [255/255, 255/255, 255/255, 1]
            padding: 20
            spacing: 30
            orientation: "vertical"

            MDLabel:
                text:'Sign Up'
                font_size: 45
                halign:'center'
                size_hint_y:  None
                height: self.texture_size[1]
                padding_y: 15
            MDTextField:
                id:signup_email
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Email'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'at'
                icon_right_color: app.theme_cls.primary_color
                required: True
            MDTextField:
                id:signup_username
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Username'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'account'
                icon_right_color: app.theme_cls.primary_color
                required: True
            MDTextField:
                id:signup_password
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Password'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'key-variant'
                icon_right_color: app.theme_cls.primary_color
                required: True
                password: True
            MDFillRoundFlatButton:
                text: "REGISTER"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                font_size: 20
                on_press: 
                    app.signup()
                    root.manager.transition.direction = 'down'
            MDRoundFlatButton:
                text: 'Already have an account? Sign In'
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press:
                    root.manager.current = 'loginscreen'
                    root.manager.transition.direction = 'down'

<ForgotPasswordScreen>:
    name: 'forgotpasswordscreen'

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        MDCard:
            size_hint: None, None
            size: 320, 500
            pos_hint:   {"center_x": 0.5, "center_y": 0.5}
            elevation: 15
            md_bg_color: [255/255, 255/255, 255/255, 1]
            padding: 20
            spacing: 30
            orientation: "vertical"

            MDLabel:
                text:'Forogt your password?'
                font_size: 45
                halign:'center'
                size_hint_y:  None
                height: self.texture_size[1]
                padding_y: 15
            MDLabel:
                text:"Confirm your emial and we'll send the instructions"
                font_size: 20
                halign:'center'
                size_hint_y:  None
                height: self.texture_size[1]
                padding_y: 15
            MDTextField:
                id: reset_email
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Email'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'at'
                icon_right_color: app.theme_cls.primary_color
                required: True
            MDFillRoundFlatButton:
                text: "Reset password"
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                font_size: 20
                on_press: 
                    app.forgot_password()
                    #root.manager.current = 'loginscreen'
                    #root.manager.transition.direction = 'right'
            MDRoundFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press:
                    app.back_to_login()
                    #root.manager.current = 'loginscreen'
                    #root.manager.transition.direction = 'right'


<MainScreen>:
    name: 'mainscreen'


    Screen:



    NavigationLayout:
        ScreenManager:
            Screen:


                BoxLayout:
                    orientation: 'vertical'
                    #anchor_x: "right"

                    MDToolbar:
                        id: tollbar
                        title: 'Shopping assistant'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state(new_state='toggle')]]      #toggle_nav_drawer()]]
                        right_action_items: [["refresh", lambda x: app.refresh_lists()]]
                        elevation:5
                    #Widget:

                    ScrollView:


                        MDList:
                            id: md_list2
                            padding: 0

                    #AnchorLayout:
                        #anchor_x: "right"
                        #anchor_y: "bottom"

                    MDRectangleFlatIconButton:               
                        id: add_new_list
                        pos_hint : {'center_x':0.5}
                        #pos_hint: {"x": .5}
                        #pos_hint_x: window.width
                        size_hint_x: 1
                        text_hint: {"x": .5}
                        text: "Add new list"
                        text_color: 0, 0, 0, 1
                        icon: "plus"
                        md_bg_color: app.theme_cls.primary_color
                        #elevation_normal: 8
                        halign: "center"
                        on_press:
                            root.manager.current = 'addnewlist'
                            root.manager.transition.direction = 'up'


        MDNavigationDrawer:
            id: nav_drawer


            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"



                Image:
                    id: avatar
                    pos_hint : {'center_x':0.5,'center_y':0.5}
                    size_hint: None, None #(1,1)
                    size: "56dp", "56dp"
                    source: "unnamed.png"
                    halign: "center"
                MDLabel:
                    id: username
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                    halign: "center"
                MDLabel:
                    id: email
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                    halign: "center"
                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Calendar"
                                on_press:
                                    app.show_calendar()
                                    root.manager.current = 'calendarscreen'
                                    root.manager.transition.direction = 'right'    
                                IconLeftWidget:
                                    icon: "calendar"

                            OneLineIconListItem:
                                text: "Friends"
                                on_press:
                                    root.manager.current = 'friendsscreen'
                                    root.manager.transition.direction = 'right'    
                                IconLeftWidget:
                                    icon: "account-multiple"

                            OneLineIconListItem:
                                text: "Theme color"
                                on_press:
                                    app.show_themepicker() 
                                IconLeftWidget:
                                    icon: "palette"

                            OneLineIconListItem:
                                text: "Reset password"
                                on_press:
                                    root.manager.current = 'resetpassword'
                                    root.manager.transition.direction = 'right'
                                IconLeftWidget:
                                    icon: "lock-reset"

                            OneLineIconListItem:
                                text: "Delete account"
                                on_press:
                                    root.manager.current = 'deleteaccount'
                                    root.manager.transition.direction = 'right'    
                                IconLeftWidget:
                                    icon: "delete"

                            OneLineIconListItem:
                                text: "Logout"
                                on_press:
                                    app.logout_dialog()
                                    root.manager.transition.direction = 'up'
                                IconLeftWidget:
                                    icon: "logout"

<ResetPassword>
    name: "resetpassword"

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        MDCard:
            size_hint: None, None
            size: 320, 540
            pos_hint:   {"center_x": 0.5, "center_y": 0.5}
            elevation: 15
            #md_bg_color: [151/255, 218/255, 250/255, 1]
            padding: 20
            spacing: 30
            orientation: "vertical"

            MDLabel:
                text:'Reset Password'
                halign:'center'
                font_size: 45
                size_hint_y:  None
                height: self.texture_size[1]
                padding_y: 15
            MDTextField:
                id: reset_email
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Email'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'account'
                icon_right_color: app.theme_cls.primary_color
                required: True
            MDTextField:
                id:reset_oldpassword
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Old Password'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'key-variant'
                icon_right_color: app.theme_cls.primary_color
                required: True
                password: True
            MDTextField:
                id:reset_newpassword
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'New Password'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'key-variant'
                icon_right_color: app.theme_cls.primary_color
                required: True
                password: True
            MDFillRoundFlatButton:
                text:'RESET'
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                font_size: 20
                on_press: 
                    app.reset_password()
                    root.manager.transition.direction = 'right'
            MDRoundFlatButton:
                text: "Back"
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press:
                    root.manager.current = 'mainscreen'
                    root.manager.transition.direction = 'left'

<DeleteAccount>
    name: 'deleteaccount'

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        MDCard:
            size_hint: None, None
            size: 320, 500
            pos_hint:   {"center_x": 0.5, "center_y": 0.5}
            elevation: 15
            #md_bg_color: [151/255, 218/255, 250/255, 1]
            padding: 20
            spacing: 30
            orientation: "vertical"

            MDLabel:
                text:'Delete Account'
                halign:'center'
                font_size: 45
                size_hint_y:  None
                height: self.texture_size[1]
                padding_y: 15
            MDTextField:
                id: delete_email
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Email'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'account'
                icon_right_color: app.theme_cls.primary_color
                required: True
            MDTextField:
                id:delete_password
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Password'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'key-variant'
                icon_right_color: app.theme_cls.primary_color
                required: True
                password: True
            MDFillRoundFlatButton:
                text:'DELETE'
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                font_size: 20
                on_press: 
                    app.delete_account()
                    #root.nav_drawer.set_state("close")
                    root.manager.transition.direction = 'up'
            MDRoundFlatButton:
                text: "Cancel"
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press:
                    root.manager.current = 'mainscreen'
                    root.manager.transition.direction = 'left'

<SwipeToDeleteItem>:
    id: swipe
    size_hint_y: None
    height: content.height
    anchor: "right"
    type_swipe: "hand"

    MDCardSwipeLayerBox:
        padding: "8dp"
        #pos_hint: {"x": .9}

        AnchorLayout:
            anchor_x: "right"

            MDIconButton:
                icon: "trash-can"
                pos_hint: {"center_y": .5}
                on_release: 
                    app.remove_item(root)

    MDCardSwipeFrontBox:
        id: item_added_color
        md_bg_color: [255/255, 255/255, 255/255, 1]

        OneLineAvatarListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            #on_press:
                #app.open_list(root)

            IconLeftWidget:
                icon: "check"
                on_press:
                    app.item_added_to_basket(root)

<MainLists>:
    size_hint_y: None
    height: content.height
    anchor: "right"
    type_swipe: "hand"

    MDCardSwipeFrontBox:

        OneLineAvatarListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            on_press:
                app.open_list(root)

            IconLeftWidget:
                icon: "clipboard-list-outline"


<AddNewList>:
    name: "addnewlist"

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        MDCard:
            size_hint: None, None
            size: 280, 460
            pos_hint:   {"center_x": 0.5, "center_y": 0.5}
            elevation: 15
            #md_bg_color: [151/255, 218/255, 250/255, 1]
            padding: 20
            spacing: 30
            orientation: "vertical"

            MDLabel:
                text:'Create new shopping list'
                halign:'center'
                font_size: 45
                size_hint_y:  None
                height: self.texture_size[1]
                padding_y: 15
            MDTextField:
                id: new_list_name
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: 220
                font_size: 20
                hint_text: 'Name of list'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'clipboard-list-outline'
                icon_right_color: app.theme_cls.primary_color
                required: True


            MDFillRoundFlatButton:
                text:'CREATE'
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                font_size: 20
                on_press:
                    app.create_new_list()


            #ScrollView:
                #MDDataTable:


            MDRoundFlatButton:
                text: "Cancel"
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press:
                    root.manager.current = 'mainscreen'
                    root.manager.transition.direction = 'down'

<ListScreen>:
    name: "listscreen"

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                id: created_list
                left_action_items: [["arrow-left", lambda x: app.back_to_main()]]
                right_action_items: [["image", lambda x: app.go_to_recognition_screen()]] 
                elevation:5




            ScrollView:

                MDList:
                    id: items_list
                    padding: 0

            MDRectangleFlatIconButton:               
                id: add_new_item_button
                pos_hint : {'center_x':0.5}
                size_hint_x: 1
                text_hint: {"x": .5}
                text: "Add new item"
                text_color: 0, 0, 0, 1
                icon: "plus"
                md_bg_color: app.theme_cls.primary_color
                halign: "center"
                on_press:
                    app.popular_items()
                    root.manager.current = 'addnewitemscreen'
                    root.manager.transition.direction = 'left'

            MDRectangleFlatIconButton:               
                id: delete_checked_items
                pos_hint : {'center_x':0.5}
                size_hint_x: 1
                text_hint: {"x": .5}
                text: "Delete checked items"
                text_color: 0, 0, 0, 1
                icon: "trash-can-outline"
                md_bg_color: app.theme_cls.primary_color
                halign: "center"
                on_press:
                    app.remove_checked_items()


            MDBottomNavigation:
                #panel_color: app.theme_cls.primary_color
                size_hint_y: .15
                text_color_normal: [0/255, 0/255, 0/255, 1]

                MDBottomNavigationItem:
                    #name: 'screen 1'
                    #text: 'Python'
                    icon: 'rename-box'
                    icon_color: app.theme_cls.primary_color
                    on_tab_press:
                        root.manager.current = 'renamelistscreen'
                        root.manager.transition.direction = 'down'


                MDBottomNavigationItem:
                    #name: 'screen 2'
                    #text: 'C++'
                    icon: 'calendar'
                    icon_color: app.theme_cls.primary_color
                    on_tab_press:
                        #app.set_time()
                        app.set_date()



                MDBottomNavigationItem:
                    #name: 'screen 2'
                    #text: 'C++'
                    icon: 'send'
                    on_tab_press:
                        app.show_friends_to_pick()
                        root.manager.current = 'pickfriendscreen'
                        root.manager.transition.direction = 'down'


                MDBottomNavigationItem:
                    #name: 'screen 3'
                    #text: 'trashcan'
                    icon: 'trash-can'
                    on_tab_press:
                        app.delete_list_dialog()


<AddNewItemScreen>
    name: "addnewitemscreen"

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                id: adding_items_toolbar
                left_action_items: [["arrow-left", lambda x: app.back_to_list()]]
                elevation:5

            MDTextField:
                id:add_new_item
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                #width: 220
                font_size: 20
                hint_text: 'Add new item'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                #icon_right: 'account'
                #icon_right_color: app.theme_cls.primary_color
                #required: True

            MDRectangleFlatIconButton:               
                id: add_new_item_button
                pos_hint : {'center_x':0.5}
                size_hint_x: 1
                text_hint: {"x": .5}
                text: "Add new item"
                text_color: 0, 0, 0, 1
                icon: "plus"
                md_bg_color: app.theme_cls.primary_color
                halign: "center"
                on_press:
                    app.add_new_item()
                    #root.manager.current = 'addnewitemscreen'
                    #root.manager.transition.direction = 'left'

            MDProgressBar:
                value: 100
                size_hint_y: .1

            MDLabel:
                text: "Most popular items which don't belong to your list"
                md_bg_color: [0/255, 1/255, 0/255, 1]
                halign: "center"
                size_hint_y: .1

            MDProgressBar:
                value: 100
                size_hint_y: .1

            ScrollView:

                MDList:
                    id: popular_items
                    halign: "center"
                    padding: 0

<CalendarScreen>:
    name: "calendarscreen"

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                id: calendar_toolbar
                title: "Calendar"
                right_action_items: [["arrow-right", lambda x: app.back_to_list_from_calendar()]]
                elevation:5


            ScrollView:

                BoxLayout:
                    orientation: "vertical"

                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    MDLabel:
                        id: first_day_label
                        #md_bg_color: [0/255, 255/255, 0/255, 1]
                        halign: "center"
                        size_hint_y: .15
                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    ScrollView:
                        MDList:
                            id: first_day_list

                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    MDLabel:
                        id: second_day_label
                        md_bg_color: [0/255, 255/255, 0/255, 1]
                        halign: "center"
                        size_hint_y: .15
                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    ScrollView:
                        MDList:
                            id: second_day_list

                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    MDLabel:
                        id: third_day_label
                        md_bg_color: [0/255, 1/255, 0/255, 1]
                        halign: "center"
                        size_hint_y: .15
                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    ScrollView:
                        MDList:
                            id: third_day_list

                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    MDLabel:
                        id: fourth_day_label
                        md_bg_color: [0/255, 1/255, 0/255, 1]
                        halign: "center"
                        size_hint_y: .15
                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    ScrollView:
                        MDList:
                            id: fourth_day_list

                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    MDLabel:
                        id: fifth_day_label
                        md_bg_color: [0/255, 1/255, 0/255, 1]
                        halign: "center"
                        size_hint_y: .15
                    MDProgressBar:
                        value: 100
                        size_hint_y: .15
                    ScrollView:
                        MDList:
                            id: fifth_day_list

<CalendarWidget>
    size_hint_y: None
    height: content.height
    anchor: "right"
    type_swipe: "hand"

    MDCardSwipeFrontBox:

        OneLineAvatarIconListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            on_press:
                app.open_list(root)
                app.remove_calendar()

            IconRightWidget:
                icon: "trash-can"
                on_press:
                    app.remove_calendar_widget(root)

            IconLeftWidget:
                icon: "clipboard-list-outline"


<PopularItems>:
    size_hint_y: None
    height: content.height
    anchor: "right"
    type_swipe: "hand"

    MDCardSwipeLayerBox:
        padding: "8dp"
        #pos_hint: {"x": .9}

        AnchorLayout:
            anchor_x: "right"

            MDIconButton:
                icon: "plus-thick"
                pos_hint: {"center_y": .5}
                on_release: 
                    app.add_popular_item(root)

    MDCardSwipeFrontBox:

        OneLineAvatarListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            #on_press:
                #app.add_popular_item(root)

            IconLeftWidget:
                icon: "chevron-right"

<RenameListScreen>:
    name:'renamelistscreen'

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        MDCard:
            #size_hint: 0.6, 0.5
            #size_hint_x: 0.8
            #size_hint_y: 0.8
            size_hint: None, None
            size: 320, 380
            pos_hint:   {"center_x": 0.5, "center_y": 0.5}
            elevation: 15
            #md_bg_color: [151/255, 218/255, 250/255, 1]
            padding: 20
            spacing: 30
            orientation: "vertical"

            MDLabel:
                text:'Rename list name'
                halign:'center'
                font_size: 45
                size_hint_y:  None
                #size_hint_x: .8
                height: self.texture_size[1]
                padding_y: 15

            MDTextField:
                id: new_list_name
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                #size_hint_x: .8
                font_size: 20
                hint_text: 'New name'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'rename-box'
                icon_right_color: app.theme_cls.primary_color
                required: True


            MDFillRoundFlatButton:
                text:'RENAME'
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                font_size: 20
                on_press:
                    app.rename_list()


            MDRoundFlatButton:
                text: "Cancel"
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press:
                    root.manager.current = 'listscreen'
                    root.manager.transition.direction = 'up'

<ShareListScreen>:
    name:'sharelistscreen'

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        MDCard:
            size_hint: None, None
            size: 320, 520
            pos_hint:   {"center_x": 0.5, "center_y": 0.5}
            elevation: 15
            #md_bg_color: [151/255, 218/255, 250/255, 1]
            padding: 20
            spacing: 30
            orientation: "vertical"

            MDLabel:
                text:'Share your list with friend'
                halign:'center'
                font_size: 45
                size_hint_y:  None
                #size_hint_x: .8
                height: self.texture_size[1]
                padding_y: 15

            MDTextField:
                id: share_list_user
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                #size_hint_x: .8
                font_size: 20
                hint_text: "Friend's email"
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'at'
                icon_right_color: app.theme_cls.primary_color
                #required: True

            MDTextField:
                id: custom_list
                pos_hint: {'center_x':0.5}
                size_hint_x: None
                width: 220
                #size_hint_x: .8
                font_size: 20
                hint_text: "Custom name"
                helper_text:'Required'
                helper_text_mode:  'on_error'
                icon_right: 'rename-box'
                icon_right_color: app.theme_cls.primary_color
                #required: True


            MDFillRoundFlatButton:
                text:'SHARE'
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.8
                font_size: 20
                on_press:
                    app.share_list()
                    #root.manager.current = 'listscreen'
                    #root.manager.transition.direction = 'down'

            MDRoundFlatButton:
                text: "Cancel"
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press:
                    app.back_to_pickfriendscreen()


<FriendsScreen>
    name: "friendsscreen"

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                id: adding_items_toolbar
                title: "Friends"
                right_action_items: [["arrow-right", lambda x: app.back_to_main_from_friends()]]
                elevation:5

            MDTextField:
                id:add_new_friend
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.9
                #width: 220
                font_size: 20
                hint_text: 'Add new friend'
                helper_text:'Required'
                helper_text_mode:  'on_error'
                #icon_right: 'account'
                #required: True

            MDRectangleFlatIconButton:               
                id: add_new_friend_button
                pos_hint : {'center_x':0.5}
                size_hint_x: 1
                text_hint: {"x": .5}
                text: "Add new friend"
                text_color: 0, 0, 0, 1
                icon: "plus"
                md_bg_color: app.theme_cls.primary_color
                halign: "center"
                on_press:
                    app.add_new_friend()
                    #root.manager.current = 'addnewitemscreen'
                    #root.manager.transition.direction = 'left'

            MDProgressBar:
                value: 100
                size_hint_y: .1

            MDLabel:
                text: "Friends"
                md_bg_color: [0/255, 1/255, 0/255, 1]
                halign: "center"
                size_hint_y: .1

            MDProgressBar:
                value: 100
                size_hint_y: .1

            ScrollView: 

                MDList:
                    id: friends_list

<FriendItemSwipe>:
    id: swipe_friend
    size_hint_y: None
    height: content.height
    anchor: "right"
    type_swipe: "hand"

    MDCardSwipeLayerBox:
        padding: "8dp"
        #pos_hint: {"x": .9}

        AnchorLayout:
            anchor_x: "right"

            MDIconButton:
                icon: "trash-can"
                pos_hint: {"center_y": .5}
                on_release: 
                    app.remove_friend(root)

    MDCardSwipeFrontBox:
        id: item_added_color
        md_bg_color: [255/255, 255/255, 255/255, 1]

        OneLineAvatarListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            #on_press:
                #app.open_list(root)

            IconLeftWidget:
                icon: "account"
                #on_press:

<PickFriendScreen>:
    name: "pickfriendscreen"

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                id: adding_items_toolbar
                title: "Friends"
                right_action_items: [["arrow-right", lambda x: app.go_to_sharelistscreen()]]
                elevation:5

            MDProgressBar:
                value: 100
                size_hint_y: .1

            MDLabel:
                text: "Pick your friend or type by yourself"
                md_bg_color: [0/255, 1/255, 0/255, 1]
                halign: "center"
                size_hint_y: .1

            MDProgressBar:
                value: 100
                size_hint_y: .1

            ScrollView: 

                MDList:
                    id: pick_friend_list

            MDRectangleFlatIconButton:               
                pos_hint : {'center_x':0.5}
                size_hint_x: 1
                text_hint: {"x": .5}
                text: "Back to list"
                text_color: 0, 0, 0, 1
                icon: "arrow-down"
                md_bg_color: app.theme_cls.primary_color
                halign: "center"
                on_press:
                    app.remove_friends_to_pick()
                    root.manager.current = 'listscreen'
                    root.manager.transition.direction = 'up'

<PickFriendItem>:
    size_hint_y: None
    height: content.height
    anchor: "right"
    type_swipe: "hand"

    MDCardSwipeFrontBox:

        OneLineAvatarListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            on_press:
                app.pick_a_friend(root)

            IconLeftWidget:
                icon: "account"

<TextRecognitionScreen>
    name: "textrecognitionscreen"

    MDScreen:
        md_bg_color: [255/255, 255/255, 255/255, 1]

        BoxLayout:
            orientation: "vertical"

            MDToolbar:
                #id: 
                title: "Optical items recognition"
                right_action_items: [["image", lambda x: app.recognize_photo()]]
                elevation:5

            MDProgressBar:
                value: 100
                size_hint_y: .1

            MDLabel:
                text: "Recognized items which don't belong to list"
                md_bg_color: [0/255, 1/255, 0/255, 1]
                halign: "center"
                size_hint_y: .1

            MDProgressBar:
                value: 100
                size_hint_y: .1

            ScrollView: 

                MDList:
                    id: recognized_items

            MDRectangleFlatIconButton:               
                pos_hint : {'center_x':0.5}
                size_hint_x: 1
                text_hint: {"x": .5}
                text: "Add recognized items"
                text_color: 0, 0, 0, 1
                icon: "plus"
                md_bg_color: app.theme_cls.primary_color
                halign: "center"
                on_press:
                    app.add_recognized_items()
                    #root.manager.current = 'listscreen'
                    #root.manager.transition.direction = 'up'

            MDRectangleFlatIconButton:               
                pos_hint : {'center_x':0.5}
                size_hint_x: 1
                text_hint: {"x": .5}
                text: "Delete checked items"
                text_color: 0, 0, 0, 1
                icon: "trash-can-outline"
                md_bg_color: app.theme_cls.primary_color
                halign: "center"
                on_press:
                    app.remove_checked_recognized_items()
                    #root.manager.current = 'listscreen'
                    #root.manager.transition.direction = 'up'

            MDRectangleFlatIconButton:               
                pos_hint : {'center_x':0.5}
                size_hint_x: 1
                text_hint: {"x": .5}
                text: "Back to list"
                text_color: 0, 0, 0, 1
                icon: "arrow-down"
                md_bg_color: app.theme_cls.primary_color
                halign: "center"
                on_press:
                    #app.remove_friends_to_pick()
                    root.manager.current = 'listscreen'
                    root.manager.transition.direction = 'up'

<PickRecognizedItem>:
    id: swipe
    size_hint_y: None
    height: content.height
    anchor: "right"
    type_swipe: "hand"

    MDCard:
        id: item_added_color_2
        md_bg_color: [255/255, 255/255, 255/255, 1]

        OneLineAvatarListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
            #on_press:
                #app.open_list(root)

            IconLeftWidget:
                icon: "check"
                on_press:
                    app.check_recognized_item(root)

'''