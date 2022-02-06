import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') 

import django 
django.setup() 

from myapp.models import Lesson 

lessons = {
    "Introduction to C++, Installing VS Code, g++ & more": {
        "index": 1,
        "vid": "j8nAHeVKL08"
    },
    "Basic Structure of a C++ Program": {
        "index": 2,
        "vid": "oW2r0r_i5Ps"
    },
    "Variables & Comments in C++ in Hindi": {
        "index": 3,
        "vid": "jigb6W35zHc"
    },
    "Variable Scope & Data Types in C++ in Hindi": {
        "index": 4,
        "vid": "JrnQ-915czY"
    },
    "C++ Basic Input/Output & More": {
        "index": 5,
        "vid": "J05uoTbGOvQ"
    },
    "C++ Header files & Operators": {
        "index": 6,
        "vid": "7D5A5ZMKRWw"
    },
    "C++ Reference Variables & Typecasting": {
        "index": 7,
        "vid": "a7Wim2t053E"
    },
    "Constants, Manipulators & Operator Precedence": {
        "index": 8,
        "vid": "i3a-G6Ebh9E"
    },
    "C++ Control Structures, If Else and Switch-Case Statement": {
        "index": 9,
        "vid": "AY96XFqb934"
    },
    "For, While and do-while loops in C++": {
        "index": 10,
        "vid": "a7dfSBrTZtE"
    },
    "Break and Continue Statements in C++": {
        "index": 11,
        "vid": "DJh5NfK7h-U"
    },
    "Pointers in C++": {
        "index": 12,
        "vid": "EvYmTCx9BFs"
    },
    "Arrays & Pointers Arithmetic in C++": {
        "index": 13,
        "vid": "ePJxpxsnkGw"
    },
    "Structures, Unions & Enums in C++": {
        "index": 14,
        "vid": "jCfR7CFlzts"
    },
    "Functions & Function Prototypes in C++": {
        "index": 15,
        "vid": "RFLFX1boGwo"
    },
    "Call by Value & Call by Reference in C++": {
        "index": 16,
        "vid": "oQbyN-vDghA"
    },
    "Inline Functions, Default Arguments & Constant Arguments in C++": {
        "index": 17,
        "vid": "oVvvwEx-gBw"
    },
    "Recursions & Recursive Functions in C++": {
        "index": 18,
        "vid": "JRKs3s15Kjc"
    },
    "Function Overloading with Examples in C++": {
        "index": 19,
        "vid": "8qZb09suSHY"
    },
    "Object Oriented Programming in C++": {
        "index": 20,
        "vid": "nGJTWaaFdjc"
    },
    "Classes, Public and Private access modifiers in C++": {
        "index": 21,
        "vid": "tL8vnfFFzVQ"
    },
    "OOPs Recap & Nesting of Member Functions in C++": {
        "index": 22,
        "vid": "d363dW0AeS8"
    },
    "C++ Objects Memory Allocation & using Arrays in Classes": {
        "index": 23,
        "vid": "qq05D2yFIHA"
    },
    "Static Data Members & Methods in C++ OOPS": {
        "index": 24,
        "vid": "QcLI2zGVYFo"
    },
    "Array of Objects & Passing Objects as Function Arguments in C++": {
        "index": 25,
        "vid": "aKnc1A5NOKo"
    },
    "Friend Functions in C++": {
        "index": 26,
        "vid": "HK6gnkQIgqI"
    },
    "Friend Classes & Member Friend Functions in C++": {
        "index": 27,
        "vid": "Tk-4KUoatg8"
    },
    "More on C++ Friend Functions (Examples & Explanation)": {
        "index": 28,
        "vid": "GTJTsMR_fro"
    },
    "Constructors In C++": {
        "index": 29,
        "vid": "EEJUPXFKe8Q"
    },
    "Parameterized and Default Constructors In C++": {
        "index": 30,
        "vid": "CYXIlh5DURI"
    },
    "Constructor Overloading In C++": {
        "index": 31,
        "vid": "7BmtA-7r1Fg"
    },
    "Constructors With Default Arguments In C++": {
        "index": 32,
        "vid": "Ok-5YqcGl6c"
    },
    "Dynamic Initialization of Objects Using Constructors": {
        "index": 33,
        "vid": "c_9oCs-9fvg"
    },
    "Copy Constructor in C++": {
        "index": 34,
        "vid": "jhZjyaNO4Wo"
    },
    "Destructor in C++ in Hindi": {
        "index": 35,
        "vid": "rm4tGxWBkqs"
    },
    "Inheritance & Its Different Types with Examples in C++": {
        "index": 36,
        "vid": "RO1ZYW9NAzg"
    },
    "Inheritance Syntax & Visibility Mode in C++": {
        "index": 37,
        "vid": "Dmrc82dL7E8"
    },
    "Single Inheritance Deep Dive: Examples + Code": {
        "index": 38,
        "vid": "S1BR0xDdsyM"
    },
    "Protected Access Modifier in C++": {
        "index": 39,
        "vid": "uHkIhwUspdI"
    },
    "Multilevel Inheritance Deep Dive with Code Example in C++": {
        "index": 40,
        "vid": "BLb6-ZgxqHg"
    },
    "Multiple Inheritance Deep Dive with Code Example in C++": {
        "index": 41,
        "vid": "h3INeRqf2vU"
    },
    "Exercise on C++ Inheritance": {
        "index": 42,
        "vid": "SW36UpSdmsM"
    },
    "Ambiguity Resolution in Inheritance in C++": {
        "index": 43,
        "vid": "ZqfArYoV9Lg"
    },
    "Virtual Base Class in C++": {
        "index": 44,
        "vid": "kzMQpPX7TUY"
    },
    "Code Example Demonstrating Virtual Base Class in C++": {
        "index": 45,
        "vid": "eYV-TohBaa0"
    },
    "Constructors in Derived Class in C++": {
        "index": 46,
        "vid": "gvOO4H7j_qI"
    },
    "Solution to Exercise on Cpp Inheritance": {
        "index": 47,
        "vid": "eGhDSjWGXQc"
    },
    "Code Example: Constructors in Derived Class in Cpp": {
        "index": 48,
        "vid": "qHrnTf5DOeI"
    },
    "Initialization list in Constructors in Cpp": {
        "index": 49,
        "vid": "-Re7K7mHtv4"
    },
    "Revisiting Pointers: new and delete Keywords in CPP": {
        "index": 50,
        "vid": "2Y0b9nFA9s8"
    },
    "Pointers to Objects and Arrow Operator in CPP": {
        "index": 51,
        "vid": "ANpUQgyRPKk"
    },
    "Array of Objects Using Pointers in C++": {
        "index": 52,
        "vid": "OCmCyYxSi2I"
    },
    "this Pointer in C++": {
        "index": 53,
        "vid": "cEOfK_L4gGA"
    },
    "Polymorphism in C++": {
        "index": 54,
        "vid": "B-WWdC-H0zw"
    },
    "Pointers to Derived Classes in C++": {
        "index": 55,
        "vid": "0YQ_yhX46uk"
    },
    "Virtual Functions in C++": {
        "index": 56,
        "vid": "fB3JHNnlRfI"
    },
    "Virtual Functions Example + Creation Rules in C++": {
        "index": 57,
        "vid": "-noYyWtdXSI"
    },
    "Abstract Base Class & Pure Virtual Functions in C++": {
        "index": 58,
        "vid": "RBAWWutf0fY"
    },
    "File I/O in C++: Working with Files": {
        "index": 59,
        "vid": "Ma0P9T4nTDA"
    },
    "File I/O in C++: Reading and Writing Files": {
        "index": 60,
        "vid": "LS1zjr1wog4"
    },
    "File I/O in C++: Read/Write in the  Same Program & Closing Files": {
        "index": 61,
        "vid": "7ku2AQsWwZE"
    },
    "File I/O in C++: open() and eof() functions": {
        "index": 62,
        "vid": "U_w-RfMrX18"
    },
    "C++ Templates: Must for Competitive Programming": {
        "index": 63,
        "vid": "kKJeekDKU30"
    },
    "Writing our First C++ Template in VS Code": {
        "index": 64,
        "vid": "SuiGXMqGKak"
    },
    "C++ Templates: Templates with Multiple Parameters": {
        "index": 65,
        "vid": "8SQL9-cQmsw"
    },
    "C++ Templates: Class Templates with Default Parameters": {
        "index": 66,
        "vid": "IdY8t0n8VBs"
    },
    "C++ Function Templates & Function Templates with Parameters": {
        "index": 67,
        "vid": "YTS0ShpFsrM"
    },
    "Member Function Templates & Overloading Template Functions in C++": {
        "index": 68,
        "vid": "Y_RMNcXAM1U"
    },
    "The C++ Standard Template Library (STL)": {
        "index": 69,
        "vid": "c9iREsYpayk"
    },
    "Containers in C++ STL": {
        "index": 70,
        "vid": "m0gnToak2-g"
    },
    "Vector In C++ STL": {
        "index": 71,
        "vid": "wKDvMcJiEPM"
    },
    "List In C++ STL": {
        "index": 72,
        "vid": "OI4CXwpMBhE"
    },
    "Map In C++ STL": {
        "index": 73,
        "vid": "KwS-Vbsha1k"
    },
    "Function Objects (Functors) In C++ STL": {
        "index": 74,
        "vid": "g4AQiptpcI8"
    }
}
def populate():

    for title, value in lessons.items():
        Lesson.objects.create(title=title, video_id=value['vid'])


if __name__ == "__main__":
    print('Populating...')
    populate()
    print('Complete!')                                