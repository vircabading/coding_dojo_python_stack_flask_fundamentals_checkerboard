//////////////////////////////////////////////////
// Subj:   Coding Dojo > Web Fundamentals > HTML/CSS/JS
// Easy Bay
// By:     Virgilio D. Cabading Jr.    October 20, 2021
//////////////////////////////////////////////////

function removePopUpBar () {                                    // Function that removes the Pop Up Bar
    var barElement = document.getElementById("pop_up_bar");
    barElement.remove();
}

function changeSource () {                                      // Function change the source of main pic on hover
    document.getElementById("main_succulent").src = "assets/succulents-2.jpg"; 
}

function changeBackSource () {                                  // Function change the source of main pic back when not hovering
    document.getElementById("main_succulent").src = "assets/succulents-1.jpg";
}