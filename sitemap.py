import requests
from bs4 import BeautifulSoup
url = 'https://jiashuwu.github.io/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
htmls = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xml:lang="en" xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="google-site-verification" content="teIm-XCd6jYOghwdT81llWQSkklzJ1kK3qJhirxkBug" />
    <meta name="baidu-site-verification" content="code-7Pq1DrRjRX" />
    <meta name="viewport" content="width=1024">
    <meta name="keywords" content="Jiashu Wu, 吴嘉澍, Transfer Learning, Domain Adaptation, Deep Learning, Machine Learning, Computer Science, University of Chinese Academy of Sciences, University of Melbourne, University of Sydney, Beijing Institute of Technology, UniMelb, USYD, UCAS, BIT, Beijing, Sydney, Melbourne, Australia, 中科院, 中国科学院, 北京理工大学, 北京">
    <title>Jiashu Wu 吴嘉澍</title>
    <link rel="stylesheet" href="./Source/bootstrap.css">
    <link rel="stylesheet" href="./Source/style.css">
    <link rel="icon" href="https://jiashuwu.github.io/Resource/cas.png">
    <script>
        function darkTheme() {
            var element = document.body;
            element.classList.toggle("dark-theme");
            var abstract = document.getElementsByClassName("abs_section");
            for (var i = 0; i < abstract.length; i++) {
                if (abstract[i].style.backgroundColor==="" || abstract[i].style.backgroundColor==="rgb(241, 241, 241)") {
                    abstract[i].style.backgroundColor="rgb(97, 97, 97)";
                } else {
                    abstract[i].style.backgroundColor="rgb(241, 241, 241)";
                }
            }
            if (document.getElementById("theme-button").src == "https://jiashuwu.github.io/Resource/dark-mode.png"){
                document.getElementById("theme-button").src = "https://jiashuwu.github.io/Resource/light-mode.png";
            } else {
                document.getElementById("theme-button").src = "https://jiashuwu.github.io/Resource/dark-mode.png";
            }
        }
    </script>
    <style>
        a {
            color: #2196f3;
        }
        a:hover {
            color: #64b5f6;
        }
        .link_navigation:link {
            text-decoration: none;
        }
        .dark-theme {
            background-color: #060606;
            color: #fafafa;
        }
        .dark-theme a {
            color: #64b5f6;
        }
        .dark-theme a:hover {
            color: #bbdefb;
        }
        .abs_section {
            background-color: #f1f1f1;
            padding: 10px;
        }
    </style>
</head>



<body data-new-gr-c-s-check-loaded="14.984.0" data-gr-ext-installed="">
    <div class="container">


        <div class="row">
            <br>
        </div>
        <div class="row">
            <div class="col-md-12 top-buffer">
                <span class="heading"><font size="6.6"><a href="https://jiashuwu.github.io/">Jiashu Wu</a></font></span>
                &emsp;&emsp;
                <span class="heading"><font size="4"><a href="https://jiashuwu.github.io/#education" class="link_navigation">Education</a></font></span>
                &emsp;&emsp;
                <span class="heading"><font size="4"><a href="https://jiashuwu.github.io/#publication" class="link_navigation">Publication</a></font></span>
                &emsp;&emsp;
                <span class="heading"><font size="4"><a href="https://jiashuwu.github.io/#granted_patent" class="link_navigation">Patent</a></font></span>
                &emsp;&emsp;
                <span class="heading"><font size="4"><a href="https://jiashuwu.github.io/#award" class="link_navigation">Award</a></font></span>
                &emsp;&emsp;
                <span class="heading"><font size="4"><a href="https://jiashuwu.github.io/#cv" class="link_navigation">CV</a></font></span>
                &emsp;&emsp;
                <span class="heading"><font size="4"><a href="https://jiashuwu.github.io/#contact" class="link_navigation">Contact</a></font></span>
                &emsp;&emsp;
                <span class="heading"><img src="https://jiashuwu.github.io/Resource/dark-mode.png" alt="" width="18" height="18" id="theme-button" onclick=darkTheme()></span>
            </div>
        </div>


        <div class="row">
            <br><br>
        </div>
        <div class="row">
            <div class="col-md-10">"""
for link in soup.find_all('a'):
    if link.get('href') != "None" and link.get('href') is not None and link.get('href')[0:4] == "http":
        url = link.get('href').replace(" ", "%20")
        atag = "<a href=\"" + url + "\" target=\"_blank\">" + url + "</a>"
        htmls += atag + "\n<br>\n<br>\n"
htmls += """
            </div>
        </div>
        <div class="row">
            <br>
        </div>
        <hr>
        <footer>
        <span>Copyright Ⓒ Jiashu Wu 2022</span>
        <br><br>
</body>
</html>"""
print(htmls)
with open("sitemap.html", "w") as sitemap_html:
    sitemap_html.write(htmls)
sitemap_html.close()
