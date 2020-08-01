#!/usr/bin/env python3

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from kivy.graphics import Mesh
from functools import partial

import roll

class diceApp(App):

    def rollDice(self, *largs):
        amount = int(self.amount.text)
        sides = int(self.sides.text)
        target = int(self.target.text)
        output = roll.getRollOutput(amount, sides, target)
        self.outputText.text = output


    def build(self):

        outputLayout = BoxLayout(orientation='vertical', size_hint=(1, None), height=500)
        self.outputText = Label(font_size='20sp')
        outputLayout.add_widget(self.outputText)


        inputLayout = GridLayout(cols=2, size_hint=(1, None))
        
        amountLabel = Label(text="Amount", font_size='20sp')
        self.amount = TextInput()
        inputLayout.add_widget(amountLabel)
        inputLayout.add_widget(self.amount)

        sidesLabel = Label(text="Sides", font_size='20sp')
        self.sides = TextInput()
        inputLayout.add_widget(sidesLabel)
        inputLayout.add_widget(self.sides)

        targetLabel = Label(text="Target", font_size='20sp')
        self.target = TextInput()
        inputLayout.add_widget(targetLabel)
        inputLayout.add_widget(self.target)


        rollLayout = BoxLayout(size_hint=(1, None), height=50)
        button = Button(text="Roll")
        button.bind(on_release=partial(self.rollDice))
        rollLayout.add_widget(button)
            

        root = BoxLayout(orientation='vertical')
        root.add_widget(outputLayout)
        root.add_widget(inputLayout)
        root.add_widget(rollLayout)

        return root


if __name__ == '__main__':
    diceApp().run()