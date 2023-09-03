    // Function to hide messages after 2 seconds
    setTimeout(function() {
        var messages = document.querySelectorAll('.alert');
        messages.forEach(function(message) {
            message.style.display = 'none';
        });
    }, 2000); // 2000 milliseconds = 2 seconds