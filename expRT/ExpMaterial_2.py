# Material


backgroundLUT = [
    {
    'name' : 'Background',
    'position' : (0, 0),
    'path' : 'OSD_ImgFolder/MainFrame.png'
    },
    {
    'name' : 'Lay_1',
    'position' : (-405, -30),
    'path' : 'OSD_ImgFolder/Layer_1.png'
    },
    {
    'name' : 'Lay_2',
    'position' : (-235, -30),
    'path' : 'OSD_ImgFolder/Layer_2.png'
    },
    {
    'name' : 'Lay_3',
    'position' : (35, -30),
    'path' : 'OSD_ImgFolder/Layer_3.png'
    },
    {
    'name' : 'Lay_4',
    'position' : (305, -30), 
    'path' : 'OSD_ImgFolder/Layer_4.png'
    }
]

optLUT = [
    {
    'layer' : 1,
    'default' : ['off', 'off', 'off', 'off', 'off'],
    'status' : ['off', 'off', 'off', 'off', 'off'],
    'path' : [{'on' : 'OSD_ImgFolder/icon1_on.png', 'off' : 'OSD_ImgFolder/icon1_off.png'}, 
              {'on' : 'OSD_ImgFolder/icon2_on.png', 'off' : 'OSD_ImgFolder/icon2_off.png'},
              {'on' : 'OSD_ImgFolder/icon3_on.png', 'off' : 'OSD_ImgFolder/icon3_off.png'},
              {'on' : 'OSD_ImgFolder/icon4_on.png', 'off' : 'OSD_ImgFolder/icon4_off.png'},
              {'on' : 'OSD_ImgFolder/icon5_on.png', 'off' : 'OSD_ImgFolder/icon5_off.png'}],
    'position' : [(-405, 110), (-405, 40), (-405, -30), (-405, -100), (-405, -170)]
    },
    {
    'layer' : 2,
    'default' : ['on', 'on', 'on', 'on', 'on'],
    # 'status' : ['on', 'on', 'on', 'on', 'on'],
    'status' : ['on', 'on', 'on', 'on', 'on'],
    'path' : [{'on' : 'OSD_ImgFolder/switch_on.png', 'off' : 'OSD_ImgFolder/switch_off.png'},
              {'on' : 'OSD_ImgFolder/radio_on.png',  'off' : 'OSD_ImgFolder/radio_off.png'},
              {'on' : 'OSD_ImgFolder/switch_on.png', 'off' : 'OSD_ImgFolder/switch_off.png'},
              {'on' : 'OSD_ImgFolder/radio_on.png',  'off' : 'OSD_ImgFolder/radio_off.png'},
              {'on' : 'OSD_ImgFolder/switch_on.png', 'off' : 'OSD_ImgFolder/switch_off.png'}],
    'position' : [(-235, 110), (-235, 40), (-235, -30), (-235, -100), (-235, -170)] 
    },
    {
    'layer' : 3,
    'default' : ['off', 'off', 'off', 'off', 'off'],
    'status' : ['off', 'off', 'off', 'off', 'off'],
    'path' : [{'on' : 'OSD_ImgFolder/radio_on.png', 'off' : 'OSD_ImgFolder/radio_off.png'},
              {'on' : 'OSD_ImgFolder/radio_on.png', 'off' : 'OSD_ImgFolder/radio_off.png'},
              {'on' : 'OSD_ImgFolder/radio_on.png', 'off' : 'OSD_ImgFolder/radio_off.png'},
              {'on' : 'OSD_ImgFolder/radio_on.png', 'off' : 'OSD_ImgFolder/radio_off.png'},
              {'on' : 'OSD_ImgFolder/radio_on.png', 'off' : 'OSD_ImgFolder/radio_off.png'}],
    'position' : [(35, 110), (35, 40), (35, -30), (35, -100), (35, -170)]
    },
    {
    'layer' : 4,
    'default' : ['off', 'off', 'off', 'off', 'off'],
    'status' : ['off', 'off', 'off', 'off', 'off'],
    'path' : [{'on' : 'OSD_ImgFolder/switch_on.png', 'off' : 'OSD_ImgFolder/switch_off.png'},
              {'on' : 'OSD_ImgFolder/switch_on.png', 'off' : 'OSD_ImgFolder/switch_off.png'},
              {'on' : 'OSD_ImgFolder/switch_on.png', 'off' : 'OSD_ImgFolder/switch_off.png'},
              {'on' : 'OSD_ImgFolder/switch_on.png', 'off' : 'OSD_ImgFolder/switch_off.png'},
              {'on' : 'OSD_ImgFolder/switch_on.png', 'off' : 'OSD_ImgFolder/switch_off.png'}],
    'position' : [(305, 110), (305, 40), (305, -30), (305, -100), (305, -170)]
    }
]


requestLUT = [
    {
     'name' : 'L1 request',
     'path' : 'OSD_ImgFolder/icon1_off.png', 
     'position' : [(-405, 110), (-405, 40), (-405, -30), (-405, -100), (-405, -170)]
    },
    {
     'name' : 'L2 request',
     'path' : 'OSD_ImgFolder/option_off.png', 
     'position' : [(-235, 110), (-235, 40), (-235, -30), (-235, -100), (-235, -170)] 
    },
    {
     'name' : 'L3 request',
     'path' : 'OSD_ImgFolder/radio_off.png', 
     'position' : [(35, 110), (35, 40), (35, -30), (35, -100), (35, -170)]
    },
    {
     'name' : 'L4 request',
     'path' : 'OSD_ImgFolder/switch_off.png', 
     'position' : [(305, 110), (305, 40), (305, -30), (305, -100), (305, -170)]
    }
]

indicatorLUT = [
    {
    'name' : 'L1 selector',
    'width' : 68,
    'height' : 70,
    'position' : [(-405, 110), (-405, 40), (-405, -30), (-405, -100), (-405, -170)]
    },
    {
    'name' : 'L2 selector',
    'width' : 268,
    'height' : 70,
    'position' : [(-235, 110), (-235, 40), (-235, -30), (-235, -100), (-235, -170)] 
    },
    {
    'name' : 'L3 selector',
    'width' : 268,
    'height' : 70,
    'position' : [(35, 110), (35, 40), (35, -30), (35, -100), (35, -170)]
    },
    {
    'name' : 'L4 selector',
    'width' : 268,
    'height' : 70,
    'position' : [(305, 110), (305, 40), (305, -30), (305, -100), (305, -170)]
    }    
]


strLUT = [
    {
    'name' : 'L1 str',
    'position' : (-405, -30),
    'path' : 'OSD_ImgFolder/aLayer_1.png'
    },
    {
    'name' : 'L2_str',
    'position' : (-235, -30),
    'path' : 'OSD_ImgFolder/L2 str.png'
    },
    {
    'name' : 'L3_str',
    'position' : (35, -30),
    'path' : 'OSD_ImgFolder/L3 str.png'
    },
    {
    'name' : 'L4_str',
    'position' : (305, -30),
    'path' : 'OSD_ImgFolder/L4 str.png'
    }
]


imageLUT = [
    {
    'name' : 'Background',
    'position' : (0, 0),
    'path' : 'OSD_ImgFolder/MainFrame.png'
    },
    {
    'name' : 'Lay_1',
    'position' : (-405, -30),
    'path' : 'OSD_ImgFolder/Layer_1.png'
    },
    {
    'name' : 'Lay_2',
    'position' : (-235, -30),
    'path' : 'OSD_ImgFolder/Layer_2.png'
    },
    {
    'name' : 'Lay_3',
    'position' : (35, -30),
    'path' : 'OSD_ImgFolder/Layer_3.png'
    },
    {
    'name' : 'Lay_4',
    'position' : (305, -30), 
    'path' : 'OSD_ImgFolder/Layer_4.png'
    }
]
