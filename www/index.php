<html>
	<head>
		<title>Rob's Projects</title>
    <style>
    .centered {
      text-align:center;
    }
    </style>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

    <script type="text/javascript">
      google.charts.load('current', {'packages':['table']});
      google.charts.setOnLoadCallback(drawTable);

      function drawTable() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Project Name');
        data.addColumn('string', 'Project Description');
        data.addColumn('string', 'Demo');
        data.addColumn('string', 'Code');

        data.addRows([
          ['Homework Manager',
           'This is a web application that allows users to schedule their schoolwork. It allows users to organize assignments in Projects and Courses.',
           "<a href='homework_manager/index.php'>Click Here</a>",
           "<a href='https://github.com/rkulesza9/Homework_Manager'>Github</a>"],

           ['SLNN',
            'I created a Convolutional Neural Network (CNN) in tensorflow and trained it with Sign Language data from this <a href="https://www.kaggle.com/datamunge/sign-language-mnist">Kaggle Dataset</a>. I was able to tweak the network against the dataset to perform at 92% accuracy over the evaluation set. I saved the best performing model to file and by clicking the link, you can demo it here or view its code.',
            "<a href='SLNN/index.php'>Click Here</a>",
            "<a href='https://github.com/rkulesza9/Sign-Language-Neural-Network'>Github</a>"],

            ['Personal Blog',
            'I created a blog to share life events as well as my enthusiasm for machine learning, programming, mathematics and more.',
            "<a href='http://robkulesza.com'>Click Here</a>",
            "<a href='https://github.com/rkulesza9/kuleszar-website'>Github</a>"],

            ['Business Page',
            'I created a business page which acts as my online resume.',
            "<a href='http://robkulesza.com/business'>Click Here</a>",
            "<a href='https://github.com/rkulesza9/kuleszar-website/tree/master/www/business'>Github</a>"],

            ['Coursework',
            'I compiled my major programming projects throughout my graduate and undergraduate experiences at kean university here. This includes a Computer Architecture assembly project, Database Management Systems graduate and undergraduate mysql php projects, and graduate and undergraduate machine learning projects.',
            "<a href='http://coursework.robkulesza.com'>Click Here</a>",
            "<a href='https://github.com/rkulesza9/kuleszar-website/tree/master/www/business'>Github</a>"],

        ]);

        var table = new google.visualization.Table(document.getElementById('table_div'));

        table.draw(data, {showRowNumber: true, width:'75%', allowHtml: true});
      }
    </script>

	</head>
	<body>
		<h1>Rob's Projects</h1>
		<p>These are projects I'm currently working on in my free time</p>
		<hr>
    <div class='centered'>
      <h2>Projects</h2>
     <div id="table_div"></div>

    </div>
	</body>
</html>
