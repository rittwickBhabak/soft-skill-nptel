import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings') 

import django 
django.setup() 

from myapp.models import Lesson 

lessons = {
    "Introduction: A New Approach To Learning": {
        "index": 1,
        "vid": "xBaLgJZ0t6A"
    },
    "Planning And Goal-Setting": {
        "index": 2,
        "vid": "pkbouY5EOHg"
    },
    "Human Perceptions: Understanding People": {
        "index": 3,
        "vid": "z6uFihRyvW4"
    },
    "Types Of Soft Skills: Self-Management Skills": {
        "index": 4,
        "vid": "9d4MpxycLyQ"
    },
    "Aiming For Excellence: Developing Potential And Self-Actualisation": {
        "index": 5,
        "vid": "W7QgPtO7NRE"
    },
    "Need Achievement And Spiritual Intelligence": {
        "index": 6,
        "vid": "D3imbW5VDSk"
    },
    "Conflict Resolution Skills: Seeking Win-Win Solution": {
        "index": 7,
        "vid": "CgShhippuP4"
    },
    "Inter-Personal Conflicts: Two Examples": {
        "index": 8,
        "vid": "CooqaYvwHG0"
    },
    "Inter-Personal Conflicts: Two Solutions": {
        "index": 9,
        "vid": "3VoDPuEW028"
    },
    "Types Of Conflicts: Becoming A Conflict Resolution Expert": {
        "index": 10,
        "vid": "4rQyD8-PNYE"
    },
    "Types Of Stress: Self-Awareness About Stress": {
        "index": 11,
        "vid": "KvEc2Emo0Ws"
    },
    "Regulating Stress: Making The Best Out Of Stress": {
        "index": 12,
        "vid": "GeckKHJqlZE"
    },
    "Habits: Guiding Principles": {
        "index": 13,
        "vid": "EOJWO2apzQA"
    },
    "Habits: Identifying Good And Bad Habits": {
        "index": 14,
        "vid": "QN_YbqiVg80"
    },
    "Habits: Habit Cycle": {
        "index": 15,
        "vid": "Y2v92ZZ-Rvk"
    },
    "Breaking Bad Habits": {
        "index": 16,
        "vid": "wpmdkGy-9vo"
    },
    "Using The Zeigarnik Effect For Productivity And Personal Growth": {
        "index": 17,
        "vid": "1qgH23QX0WY"
    },
    "Forming Habits Of Success": {
        "index": 18,
        "vid": "VLgs4DUgzVU"
    },
    "Communication: Significance Of Listening": {
        "index": 19,
        "vid": "uU8bdZ7hCXs"
    },
    "Communication: Active Listening": {
        "index": 20,
        "vid": "AM-nBU8N4So"
    },
    "Communication: Barriers To Active Listening": {
        "index": 21,
        "vid": "pv1p5Bq19DY"
    },
    "Telephone Communication: Basic Telephone Skills": {
        "index": 22,
        "vid": "Qdy-g8y6yK4"
    },
    "Telephone Communication: Advanced Telephone Skills": {
        "index": 23,
        "vid": "A4USCXJPEY0"
    },
    "Telephone Communication: Essential Telephone Skills": {
        "index": 24,
        "vid": "WfEnaZ1hzUs"
    },
    "Technology And Communication: Technological Personality?": {
        "index": 25,
        "vid": "UeDIZdUtEKQ"
    },
    "Technology And Communication: Mobile Personality?": {
        "index": 26,
        "vid": "Se_ji14zasE"
    },
    "Topic: Technology And Communication: E-Mail Principles": {
        "index": 27,
        "vid": "uSKKGdHTmak"
    },
    "Technology And Communication: How Not To Send E-Mails!": {
        "index": 28,
        "vid": "mqoewo595-4"
    },
    "Technology And Communication: Netiquette": {
        "index": 29,
        "vid": "LiWKbX_ivtQ"
    },
    "Technology And Communication: E-Mail Etiquette": {
        "index": 30,
        "vid": "pDp_-i4r__Q"
    },
    "Communication Skills: Effective Communication": {
        "index": 31,
        "vid": "ImtxyrnhrYw"
    },
    "Barriers To Communication: Arising Out Of Sender/Receiver Personality": {
        "index": 32,
        "vid": "4XbQZJwMCvU"
    },
    "Barriers To Communication: Interpersonal Transactions": {
        "index": 33,
        "vid": "O-ZqW9Tvrac"
    },
    "Barriers To Communication: Miscommunication": {
        "index": 34,
        "vid": "BupZVDV6AXI"
    },
    "Non-Verbal Communication: Pre-Thinking Assessment-1": {
        "index": 35,
        "vid": "iYjhrZo2tYY"
    },
    "Non-Verbal Communication: Pre-Thinking Assessment-2": {
        "index": 36,
        "vid": "WI8MzZxSF5o"
    },
    "Nonverbal Communication: Introduction And Importance": {
        "index": 37,
        "vid": "c24hvf-7Eh4"
    },
    "Non-Verbal Communication: Issues And Types": {
        "index": 38,
        "vid": "j_FjuhhEmCM"
    },
    "Non-Verbal Communication: Basics And Universals": {
        "index": 39,
        "vid": "7VLWiuCeS5E"
    },
    "Non-Verbal Communication: Interpreting Non-Verbal Cues": {
        "index": 40,
        "vid": "DmUCXreXb8s"
    },
    "Body Language: For Interviews": {
        "index": 41,
        "vid": "_LC0uaL3dcM"
    },
    "Body Language: For Group Discussions": {
        "index": 42,
        "vid": "3_AbGrX2PmY"
    },
    "Presentation Skills: Overcoming Fear": {
        "index": 43,
        "vid": "9nXZ8c905jo"
    },
    "Presentation Skills: Becoming A Professional": {
        "index": 44,
        "vid": "thHQTDkRsSA"
    },
    "Presentation Skills: The Role Of Body Language": {
        "index": 45,
        "vid": "qjXYrVI0xn4"
    },
    "Presentation Skills: Using Visuals": {
        "index": 46,
        "vid": "JF_m8AhkxuM"
    },
    "Reading Skills: Effective Reading": {
        "index": 47,
        "vid": "6JWblHNgCMc"
    },
    "Human Relations: Developing Trust And Integrity": {
        "index": 48,
        "vid": "p5JTuC8zpcI"
    },
    "Lecture 01: INTRODUCTION: Highlights of Developing SS Course-1-24": {
        "index": 1,
        "vid": "URtdGiutVew"
    },
    "Lecture 02: INTRODUCTION: Highlights of Developing SS Course-25-48": {
        "index": 2,
        "vid": "B0faJ4qlo3E"
    },
    "Lecture 03: MIND-SET-1: Definitions and Types": {
        "index": 3,
        "vid": "93-Jz6yI5XA"
    },
    "Lecture 04: MIND-SET-2: Learning Mindsets": {
        "index": 4,
        "vid": "aAQjzXcXe1o"
    },
    "Lecture 05: MIND-SET-3: Secrets of Developing Growth Mindsets": {
        "index": 5,
        "vid": "bwqZVvrVoT0"
    },
    "Lecture 06: Managing Time-1: Importance of Time and Understanding Perceptions of Time": {
        "index": 6,
        "vid": "XMQ65kqKmUs"
    },
    "Lecture 07: Managing Time-2: Using Time Efficiently": {
        "index": 7,
        "vid": "BPu94uS8W5Q"
    },
    "Lecture 08: Handling Delay-1: Understanding Procrastination": {
        "index": 8,
        "vid": "s5thy9KOVWc"
    },
    "Lecture 09: Handling Delay-2: Overcoming Procrastination": {
        "index": 9,
        "vid": "B6a3TpiUqwA"
    },
    "Lecture 10: Assertiveness-1: Don’t Say “Yes” to Make Others Happy!": {
        "index": 10,
        "vid": "9n_k1wvBx-M"
    },
    "Lecture 11: Assertiveness -2: Types of People": {
        "index": 11,
        "vid": "jHnMomzbLZM"
    },
    "Lecture 12: Assertiveness -3: How to Say “No”": {
        "index": 12,
        "vid": "Dyd6xvwXlWg"
    },
    "Lecture 13: Managing Negative Emotions: Controlling Anger": {
        "index": 13,
        "vid": "dAdXKtIu1lA"
    },
    "Lecture 14: Channelizing Positive Emotions-1: Gaining Power from Positive Thinking-1": {
        "index": 14,
        "vid": "xnY8ijWLVFE"
    },
    "Lecture 15: Channelizing Positive Emotions-2: Gaining Power from Positive Thinking-2": {
        "index": 15,
        "vid": "nILD1cllOpA"
    },
    "Lecture 16: People Skills-1: What Makes Others Dislike You?": {
        "index": 16,
        "vid": "1-J50E0T80I"
    },
    "Lecture 17: People Skills-2: What Makes Others Like You?-1": {
        "index": 17,
        "vid": "sTDY1H5HxqI"
    },
    "Lecture 18: People Skills-3: What Makes Others Like You?-2": {
        "index": 18,
        "vid": "xO0BzqML2P8"
    },
    "Lecture 19: People Skills-4: Being Attractive-1": {
        "index": 19,
        "vid": "HE39g_hepgE"
    },
    "Lecture 20: People Skills-5: Being Attractive-2": {
        "index": 20,
        "vid": "p7uLXZS4x2I"
    },
    "Lecture 21: English Skills-1: Common Errors-1": {
        "index": 21,
        "vid": "4F6WxMbjl5Q"
    },
    "Lecture 22: English Skills-2: Common Errors-2": {
        "index": 22,
        "vid": "Nj5m8tPYxug"
    },
    "Lecture 23: English Skills-3: Common Errors-3": {
        "index": 23,
        "vid": "rvk3nNvoe5A"
    },
    "Lecture 24: English Skills-4: Common Errors-4": {
        "index": 24,
        "vid": "B7OrKTR_9-0"
    },
    "Lecture 25: English Skills-5: Common Errors-5": {
        "index": 25,
        "vid": "puoAXPpJphQ"
    },
    "Lecture 26: Significance of Humour in Communication-1": {
        "index": 26,
        "vid": "Y7JqGpDYQb8"
    },
    "Lecture 27: Humour in Workplace": {
        "index": 27,
        "vid": "ltQGAfwAxSo"
    },
    "Lecture 28: Function of Humour in Workplace": {
        "index": 28,
        "vid": "TyLj8ZnePGs"
    },
    "Lecture 29: Money and Personality": {
        "index": 29,
        "vid": "9-ZnBXERnVo"
    },
    "Lecture 30: Managing Money": {
        "index": 30,
        "vid": "o5eD-G3X5r4"
    },
    "Lecture 31: Health and Personality": {
        "index": 31,
        "vid": "xOwGL7KtHkQ"
    },
    "Lecture 32: Managing Health-1 Importance of Exercise": {
        "index": 32,
        "vid": "xpyqd2bBYGE"
    },
    "Lecture 33: Managing Health-2 Diet and Sleep": {
        "index": 33,
        "vid": "2h47Q9vLS-s"
    },
    "Lecture 34: Love and Personality": {
        "index": 34,
        "vid": "Py0Yk2xdCQI"
    },
    "Lecture 35: Managing Love": {
        "index": 35,
        "vid": "HiQokHnoFaE"
    },
    "Lecture 36: Ethics and Etiquette": {
        "index": 36,
        "vid": "Syd1cQ7kWFU"
    },
    "Lecture 37: Business Etiquette": {
        "index": 37,
        "vid": "NqlfZOPMqjA"
    },
    "Lecture 38: Managing Mind and Memory": {
        "index": 38,
        "vid": "g_PeKz3lKU4"
    },
    "Lecture 39: Improving Memory": {
        "index": 39,
        "vid": "p7rYrbkmFyE"
    },
    "Lecture 40: Care for Environment": {
        "index": 40,
        "vid": "9Nc6spNjDvI"
    },
    "Lecture 1:": {
        "index": 1,
        "vid": "l2Wb-qfc50U"
    },
    "Lecture 2:": {
        "index": 2,
        "vid": "oUrGHwokhKk"
    },
    "Lecture 3:": {
        "index": 3,
        "vid": "xOByPSPu4NU"
    },
    "Lecture 4 :": {
        "index": 4,
        "vid": "XK36VJ2DFBM"
    },
    "Lecture 5:": {
        "index": 5,
        "vid": "aUv2HOO7eV0"
    },
    "Lecture 6:": {
        "index": 6,
        "vid": "V3WuKqAgUhY"
    },
    "Lecture 7:": {
        "index": 7,
        "vid": "r_Z4UVCACrM"
    },
    "Lecture 8 :": {
        "index": 8,
        "vid": "IhIqP-qF-d8"
    },
    "Lecture 9 :": {
        "index": 9,
        "vid": "ZQakD3ziCYY"
    },
    "Lecture 10 :": {
        "index": 10,
        "vid": "L08UaY0DV7o"
    },
    "Lecture 11": {
        "index": 11,
        "vid": "M6rGHLQNl8g"
    },
    "Lecture 12": {
        "index": 12,
        "vid": "S4w1ABMU_uE"
    },
    "Lecture 13": {
        "index": 13,
        "vid": "L7ts0QV2-hI"
    },
    "Lecture 14": {
        "index": 14,
        "vid": "RzYq-h7VcLU"
    },
    "Lecture 15 : People Skills": {
        "index": 15,
        "vid": "_WG6K_urBTs"
    },
    "Lecture 16 : People Skills (Contd.)": {
        "index": 16,
        "vid": "oLnNncwKh-E"
    },
    "Lecture 17 : People Skills (Contd.)": {
        "index": 17,
        "vid": "GybCIZKhyVU"
    },
    "Lecture 18 : People Skills (Contd.)": {
        "index": 18,
        "vid": "2TSbvpex9VQ"
    },
    "Lecture 19 : Specialised Skills": {
        "index": 19,
        "vid": "ZB6zuunf6bw"
    },
    "Lecture 20 : Specialised Skills (Contd.)": {
        "index": 20,
        "vid": "zMOQ_ekoUOs"
    },
    "Lecture 21 : Specialised Skills (Contd.)": {
        "index": 21,
        "vid": "E3OiXg224vU"
    },
    "Lecture 22 : Specialised Skills (Contd.)": {
        "index": 22,
        "vid": "482pqnghSyE"
    },
    "Lecture 23 ;": {
        "index": 23,
        "vid": "6OxSbWZVlQQ"
    },
    "Lecture 24 :": {
        "index": 24,
        "vid": "4JTxYlo_r2U"
    },
    "Lecture 25 :": {
        "index": 25,
        "vid": "2BNUqcVGnpc"
    },
    "Lecture 26 :": {
        "index": 26,
        "vid": "aeb636I2Szw"
    },
    "Lecture 27 :": {
        "index": 27,
        "vid": "YfUmnL5XyVU"
    },
    "Lecture 28 ;": {
        "index": 28,
        "vid": "Y99hdGoBh1U"
    },
    "Lecture 29 :": {
        "index": 29,
        "vid": "UTv14lqTiKs"
    },
    "Lecture 30 ;": {
        "index": 30,
        "vid": "OZHis3s1F0A"
    },
    "Lecture 31 :": {
        "index": 31,
        "vid": "QLKtX33y7fs"
    },
    "Lecture 32 :": {
        "index": 32,
        "vid": "8cDowGYD7no"
    },
    "Lecture 33": {
        "index": 33,
        "vid": "NZz4wZwjqcQ"
    },
    "Lecture 34": {
        "index": 34,
        "vid": "NB6UHLUsRfk"
    },
    "Lecture 35": {
        "index": 35,
        "vid": "FJNjgEBqeZs"
    },
    "Lecture 36": {
        "index": 36,
        "vid": "NYh_XxbhF4Q"
    },
    "Lecture 37": {
        "index": 37,
        "vid": "E-Zd_CP5nNw"
    },
    "Lecture 38": {
        "index": 38,
        "vid": "XPzdARS4uTA"
    },
    "Lecture 39": {
        "index": 39,
        "vid": "1WmbbnY5RWM"
    },
    "Lecture 40": {
        "index": 40,
        "vid": "pbgICtpIQOc"
    },
    "Lecture 41": {
        "index": 41,
        "vid": "U4n2cl-hVEI"
    },
    "mod10lec42": {
        "index": 42,
        "vid": "wgzed36Vkrk"
    },
    "mod10lec43": {
        "index": 43,
        "vid": "X37gqLPgO-U"
    },
    "mod10lec44": {
        "index": 44,
        "vid": "TEV3SxSbMgA"
    },
    "mod10lec45": {
        "index": 45,
        "vid": "3EN6TEqrJVI"
    },
    "mod10lec46": {
        "index": 46,
        "vid": "ik4yc1RUYDY"
    },
    "mod11lec47": {
        "index": 47,
        "vid": "mB3BWT0c3BE"
    },
    "mod11lec48": {
        "index": 48,
        "vid": "CqwyS0EXtZQ"
    },
    "mod11lec49": {
        "index": 49,
        "vid": "K6vGgh3GQJI"
    },
    "mod11lec50": {
        "index": 50,
        "vid": "2SCND-qcfrA"
    },
    "mod11lec51": {
        "index": 51,
        "vid": "bvLHvOmT-dk"
    },
    "mod12lec52": {
        "index": 52,
        "vid": "Bp3rOv_vl-g"
    },
    "mod12lec53": {
        "index": 53,
        "vid": "7e_Bzg133F4"
    },
    "mod12lec54": {
        "index": 54,
        "vid": "VG3MIGLjILM"
    },
    "mod12lec55": {
        "index": 55,
        "vid": "UF5iH5bW1Lk"
    },
    "mod12lec56": {
        "index": 56,
        "vid": "WTQsPEeKS84"
    }
}

def populate():

    for title, value in lessons.items():
        Lesson.objects.create(title=title, video_id=value['vid'])


if __name__ == "__main__":
    print('Populating...')
    populate()
    print('Complete!')                                