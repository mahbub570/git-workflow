# My Awesome Project

## Section 1: Feature 1

<iframe src="https://giphy.com/embed/Y4:0" width="100%" height="150px" frameborder="0" allowfullscreen></iframe>

This is the first feature of my project. It does X, Y, and Z.

## Section 2: Feature 2

<iframe src="https://giphy.com/embed/l3:0" width="100%" height="150px" frameborder="0" allowfullscreen></iframe>

This is the second feature of my project. It does A, B, and C.

## Section 3: Feature 3

<iframe src="https://giphy.com/embed/l3:0" width="100%" height="150px" frameborder="0" allowfullscreen></iframe>

This is the third feature of my project. It does D, E, and F.

<script>
function nextSection() {
    var current = document.querySelector('.active');
    var next = current.nextElementSibling;
    
    if (next) {
        current.classList.remove('active');
        next.classList.add('active');
    }
}

function prevSection() {
    var current = document.querySelector('.active');
    var prev = current.previousElementSibling;
    
    if (prev) {
        current.classList.remove('active');
        prev.classList.add('active');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var sections = document.querySelectorAll('section');
    for (var i = 0; i < sections.length; i++) {
        sections[i].addEventListener('click', function() {
            this.classList.add('active');
            var activeSection = document.querySelector('.active');
            
            // Add next button
            var nextButton = document.createElement('button');
            nextButton.textContent = 'Next';
            nextButton.style.position = 'absolute';
            nextButton.style.top = '50%';
            nextButton.style.left = '90%';
            nextButton.style.transform = 'translate(-50%, -50%)';
            nextButton.style.backgroundColor = 'transparent';
            nextButton.style.border = 'none';
            nextButton.style.cursor = 'pointer';
            nextButton.onclick = nextSection;
            
            // Add previous button
            var prevButton = document.createElement('button');
            prevButton.textContent = 'Previous';
            prevButton.style.position = 'absolute';
            prevButton.style.top = '50%';
            prevButton.style.left = '10%';
            prevButton.style.transform = 'translate(-50%, -50%)';
            prevButton.style.backgroundColor = 'transparent';
            prevButton.style.border = 'none';
            prevButton.style.cursor = 'pointer';
            prevButton.onclick = prevSection;
            
            activeSection.appendChild(nextButton);
            activeSection.appendChild(prevButton);
        });
    }
});
</script>
