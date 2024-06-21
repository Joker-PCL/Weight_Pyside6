<!-- ########### Example ########### -->
    - https://youtu.be/TP1eUsSMoBs?si=pW1v3e3p2M26bULp

<!-- ssh -->
    ** ลบ ssh-keygen
        - ssh-keygen -R 192.168.10.7
    ** remote ssh
        - ssh joker@192.168.10.7
    ** ส่งไฟล์
        - scp VideoPlayer.py polipharm@192.168.10.7:/home/polipharm/Desktop
        
<!-- ########### compile pyside6 project ########### -->
    - pyside6-uic weight.ui > ui_weight.py
    - pyside6-rcc resource.qrc -o resource_rc.py
    ** convert ui_weight.py flie to UTF-8 before

    - cd my_project
    ** windows
        - python -m venv .env
        - env\Scripts\activate
    ** linux
        - python3 -m venv env
        - source env/bin/activate
        - pip3 install gpiozero
        - python3 -m venv --system-site-packages env 

<!-- ########### Libraries ########### -->
    ** pyside6
        - pip install pyside6

    ** Install front kanit
        .assets/fronts/kanit.zip
        cd fonts
        - mkdir /usr/share/fonts/kanit
        - mv *.ttf /usr/share/fonts/kanit
        - cd /usr/share/fonts/kanit
        - mkfontscale
        - mkfontdir
        - fc-cache
        - xset fp rehash

    ** Libraries
        - pip install google-api-python-client
        - pip install google-auth-oauthlib
        - pip install pywifi
        - pip install comtypes
        - pip install requests
        - pip install pyserial