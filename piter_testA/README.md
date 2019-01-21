<body>
<!-- -->

<h2>Python + Pytest + Selenium + Allure automation test project</h2>


<div>
<h3>To integrate PyCharm with PyTest</h3>
<p>Preferences -> Tools -> Default test runner -> PyCharm</p>
<div>

<div>
<h3>Создание контейнера </h3>
<p>Для создания контейнера, нужно находясь внутри директории learn_Python  выполнить команду: docker build -t my_test:v0.2 piter_testA/</p>
<p>Метка и версия могут быть произвольными</p>
<div>


<div>
<h3>To generate HTML report:</h3>
<p>pytest --html=report.html<p>
</div>

<div>
<h3>To generate allure report</h3>
<p>pytest --alluredir ./my-allure<p>
<p>allure generate ./my-allure</p>
</div>
</body>
