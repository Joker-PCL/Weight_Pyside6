<!--  Example  -->
    - https://youtu.be/TP1eUsSMoBs?si=pW1v3e3p2M26bULp

<!-- วิธีการ รีโมทผ่าน ssh -->
    ** ลบ ssh-keygen
        - ssh-keygen -R 192.168.10.7
    ** remote ssh
        - ssh polipharm@192.168.10.7
    ** ส่งไฟล์
        - scp main.py polipharm@192.168.10.7:/home/polipharm/Desktop
        
<!--  building and deploying Qt for Python applications.  -->
    - pyside6-uic weight10s_10inch.ui > ui_weight_10inch.py
    - pyside6-uic weightIPC_10inch.ui > ui_weight_10inch.py
    - pyside6-rcc resource.qrc -o resource_rc.py
    ** convert ui_weight_10inch.py flie to UTF-8 before

<!-- ติดตั้ง environment -->
    - cd polipharm

    ** windows
        - python -m venv env
        - env\Scripts\activate
        - python3 -m venv --system-site-packages env 
    ** linux
        - python3 -m venv env
        - source env/bin/activate
        - pip3 install gpiozero
        - python3 -m venv --system-site-packages env 

<!-- ติดตั้ง Libraries -->
    ** pyside6
        - pip install pyside6

    ** Install front kanit
        .assets/fronts/kanit.zip
        cd fonts
        - sudo mkdir /usr/share/fonts/kanit
        - sudo mv *.ttf /usr/share/fonts/kanit
        - cd /usr/share/fonts/kanit
        - sudo mkfontscale
        - sudo mkfontdir
        - fc-cache
        - xset fp rehash

    ** Libraries
        - pip install google-api-python-client
        - pip install google-auth-oauthlib
        - pip install pywifi
        - pip install comtypes
        - pip install requests
        - pip install pyserial