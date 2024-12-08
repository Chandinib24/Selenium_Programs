{
  "id": "669fe9f2-373b-4943-a3f5-7fc5eedba8c9",
  "version": "2.0",
  "name": "Cura_health",
  "url": "https://katalon-demo-cura.herokuapp.com",
  "tests": [{
    "id": "707f48a2-6135-48b5-8837-73e8863c48e2",
    "name": "Positive TC 1 cura",
    "commands": [{
      "id": "98ab60cd-b4c9-4588-9363-fb9a7b531020",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "7be61639-1796-4afa-823f-94e5fcee19b5",
      "comment": "",
      "command": "setWindowSize",
      "target": "1050x708",
      "targets": [],
      "value": ""
    }, {
      "id": "39a72018-65ac-419c-a003-b77237929f20",
      "comment": "",
      "command": "click",
      "target": "id=btn-make-appointment",
      "targets": [
        ["id=btn-make-appointment", "id"],
        ["linkText=Make Appointment", "linkText"],
        ["css=#btn-make-appointment", "css:finder"],
        ["xpath=//a[contains(text(),'Make Appointment')]", "xpath:link"],
        ["xpath=//a[@id='btn-make-appointment']", "xpath:attributes"],
        ["xpath=//header[@id='top']/div/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, './index.php#appointment')]", "xpath:href"],
        ["xpath=//div/a", "xpath:position"],
        ["xpath=//a[contains(.,'Make Appointment')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "dee94fc8-0155-4115-b416-78c6859f0b62",
      "comment": "",
      "command": "click",
      "target": "id=btn-book-appointment",
      "targets": [
        ["id=btn-book-appointment", "id"],
        ["css=#btn-book-appointment", "css:finder"],
        ["xpath=//button[@id='btn-book-appointment']", "xpath:attributes"],
        ["xpath=//section[@id='appointment']/div/div/form/div[6]/div/button", "xpath:idRelative"],
        ["xpath=//button", "xpath:position"],
        ["xpath=//button[contains(.,'Book Appointment')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "dc841aea-47ca-4b29-b1c8-0a539ed18e42",
      "comment": "",
      "command": "click",
      "target": "css=.fa-bars",
      "targets": [
        ["css=.fa-bars", "css:finder"],
        ["xpath=//a[@id='menu-toggle']/i", "xpath:idRelative"],
        ["xpath=//i", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ab3cc729-9d89-4622-b349-e1dc121caacb",
      "comment": "",
      "command": "click",
      "target": "linkText=Logout",
      "targets": [
        ["linkText=Logout", "linkText"],
        ["css=li:nth-child(6) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Logout')]", "xpath:link"],
        ["xpath=(//a[@onclick=\"$('#menu-close').click();\"])[5]", "xpath:attributes"],
        ["xpath=//nav[@id='sidebar-wrapper']/ul/li[5]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'authenticate.php?logout')]", "xpath:href"],
        ["xpath=//li[5]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Logout')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "4e569fdd-6780-4601-8701-e7cc4b3ed4c0",
      "comment": "",
      "command": "click",
      "target": "id=btn-make-appointment",
      "targets": [
        ["id=btn-make-appointment", "id"],
        ["linkText=Make Appointment", "linkText"],
        ["css=#btn-make-appointment", "css:finder"],
        ["xpath=//a[contains(text(),'Make Appointment')]", "xpath:link"],
        ["xpath=//a[@id='btn-make-appointment']", "xpath:attributes"],
        ["xpath=//header[@id='top']/div/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, './profile.php#login')]", "xpath:href"],
        ["xpath=//div/a", "xpath:position"],
        ["xpath=//a[contains(.,'Make Appointment')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "4a324b04-02a2-469c-abc0-ade279e45818",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,500)",
      "targets": [],
      "value": ""
    }, {
      "id": "65d9c900-9058-46fd-b8b5-51af0d430c21",
      "comment": "",
      "command": "click",
      "target": "css=.col-sm-8:nth-child(2) > .input-group > .form-control",
      "targets": [
        ["css=.col-sm-8:nth-child(2) > .input-group > .form-control", "css:finder"],
        ["xpath=//input[@value='John Doe']", "xpath:attributes"],
        ["xpath=//section[@id='login']/div/div/div[2]/form/div/div/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f75f502e-2843-4891-acdc-3333e9caf399",
      "comment": "",
      "command": "click",
      "target": "id=txt-username",
      "targets": [
        ["id=txt-username", "id"],
        ["name=username", "name"],
        ["css=#txt-username", "css:finder"],
        ["xpath=//input[@id='txt-username']", "xpath:attributes"],
        ["xpath=//section[@id='login']/div/div/div[2]/form/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "25dc9aa7-d482-459b-ba9c-725f66e9efa3",
      "comment": "",
      "command": "type",
      "target": "id=txt-username",
      "targets": [
        ["id=txt-username", "id"],
        ["name=username", "name"],
        ["css=#txt-username", "css:finder"],
        ["xpath=//input[@id='txt-username']", "xpath:attributes"],
        ["xpath=//section[@id='login']/div/div/div[2]/form/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": "John Doe"
    }, {
      "id": "c975183d-45b1-4c11-a074-eea16dbddf4f",
      "comment": "",
      "command": "click",
      "target": "css=.alert",
      "targets": [
        ["css=.alert", "css:finder"],
        ["xpath=//section[@id='login']/div/div/div[2]/form/div", "xpath:idRelative"],
        ["xpath=//form/div", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9a1d93c1-feb5-4035-830e-d339250cea16",
      "comment": "",
      "command": "click",
      "target": "id=txt-password",
      "targets": [
        ["id=txt-password", "id"],
        ["name=password", "name"],
        ["css=#txt-password", "css:finder"],
        ["xpath=//input[@id='txt-password']", "xpath:attributes"],
        ["xpath=//section[@id='login']/div/div/div[2]/form/div[3]/div/input", "xpath:idRelative"],
        ["xpath=//div[3]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "94d7b056-a853-41ca-8d4f-4d6d1011de68",
      "comment": "",
      "command": "type",
      "target": "id=txt-password",
      "targets": [
        ["id=txt-password", "id"],
        ["name=password", "name"],
        ["css=#txt-password", "css:finder"],
        ["xpath=//input[@id='txt-password']", "xpath:attributes"],
        ["xpath=//section[@id='login']/div/div/div[2]/form/div[3]/div/input", "xpath:idRelative"],
        ["xpath=//div[3]/div/input", "xpath:position"]
      ],
      "value": "ThisIsNotAPassword"
    }, {
      "id": "37dec705-4307-4f1b-be4e-4e27096dd281",
      "comment": "",
      "command": "click",
      "target": "id=btn-login",
      "targets": [
        ["id=btn-login", "id"],
        ["css=#btn-login", "css:finder"],
        ["xpath=//button[@id='btn-login']", "xpath:attributes"],
        ["xpath=//section[@id='login']/div/div/div[2]/form/div[4]/div/button", "xpath:idRelative"],
        ["xpath=//button", "xpath:position"],
        ["xpath=//button[contains(.,'Login')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b6f4d04f-5d58-4463-b0f0-91d82fe95500",
      "comment": "",
      "command": "close",
      "target": "",
      "targets": [],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "6d42da05-4f68-4590-af04-24f7f8221144",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["707f48a2-6135-48b5-8837-73e8863c48e2"]
  }],
  "urls": ["https://katalon-demo-cura.herokuapp.com/"],
  "plugins": []
}
