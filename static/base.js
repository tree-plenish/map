function expandNavbar() {
    var x = document.getElementById("topnav");
    if (x.className === "nav") {
      x.className += " responsive";
      document.getElementById("mapid").classList.add("underNav");
    } else {
      x.className = "nav";
      document.getElementById("mapid").classList.remove("underNav");
    }

  }