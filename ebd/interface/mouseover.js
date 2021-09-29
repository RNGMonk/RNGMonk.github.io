      // Javascript Animation
      // Script Genereated by Eyeball Animation code generator
      // http://www.eyeball-design.com (freebie section)

      <!-- hide 

      browserName = navigator.appName; 
      browserVer = parseInt(navigator.appVersion); 
      browser = "NotOk"; 
	previous=0;

      // Detect if Netscape or MSIE version is ok 

      if (browserName == "Netscape" && browserVer >= 3) { browser = "ok"} 
      if (browserName == "Microsoft Internet Explorer" && browserVer >= 4) { browser =
      "ok"} 

      // Initialize your images

      if (browser == "ok") { 

	     bOn = new Image(); bOn.src = "images/interface/bulleton.gif";	
	     bOff = new Image(); bOff.src = "images/interface/bullet.gif";

	     bt01 = new Image(); bt01.src = "images/interface/button01.gif";
	     bt01on = new Image(); bt01on.src = "images/interface/button01on.gif";
	     bt02 = new Image(); bt02.src = "images/interface/button02.gif";
	     bt02on = new Image(); bt02on.src = "images/interface/button02on.gif";
	     bt03 = new Image(); bt03.src = "images/interface/button03.gif";
	     bt03on = new Image(); bt03on.src = "images/interface/button03on.gif";
	     bt04 = new Image(); bt04.src = "images/interface/button04.gif";
	     bt04on = new Image(); bt04on.src = "images/interface/button04on.gif";
	     bt05 = new Image(); bt05.src = "images/interface/button05.gif";
	     bt05on = new Image(); bt05on.src = "images/interface/button05on.gif";
	     bt06 = new Image(); bt06.src = "images/interface/button06.gif";
	     bt06on = new Image(); bt06on.src = "images/interface/button06on.gif";
	     bt07 = new Image(); bt07.src = "images/interface/button08.gif";
	     bt07on = new Image(); bt07on.src = "images/interface/button08on.gif";


	     bk = new Image(); bk.src = "images/interface/back.gif";
	     bkon = new Image(); bkon.src = "images/interface/backon.gif";


      }

      function swap(imgName,select) 
      { if (browser == "ok") {imgOn = eval(select+ ".src"); 
      document.images[imgName].src = imgOn; }} 
