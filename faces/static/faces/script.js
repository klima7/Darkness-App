document.addEventListener('DOMContentLoaded', function() {
    // Add click event listeners to letter pair items
    const letterPairItems = document.querySelectorAll('.letter-pair-item');
    
    letterPairItems.forEach(item => {
        item.addEventListener('click', function() {
            // Toggle selected class on click
            letterPairItems.forEach(i => i.classList.remove('selected'));
            this.classList.add('selected');
            
            // You could add more functionality here, such as showing details in a modal
        });
        
        // Add double click event listener to open admin edit view
        item.addEventListener('dblclick', function() {
            const pairId = this.dataset.pairId;
            if (pairId) {
                openPairAdmin(pairId);
            }
        });
    });
    
    // Function to open pair in admin
    function openPairAdmin(pairId) {
        window.location.href = `/admin/core/pair/${pairId}/change/`;
    }
    
    // Add change event listener to letter select dropdown
    const letterSelect = document.getElementById('letter-select');
    if (letterSelect) {
        letterSelect.addEventListener('change', function() {
            const selectedLetter = this.value;
            const urlPattern = document.getElementById('url-pattern').value;
            const redirectUrl = urlPattern.replace('PLACEHOLDER', selectedLetter);
            window.location.href = redirectUrl;
        });
    }
    
    // Function to resize tiles based on container height and number of items
    function resizeTiles() {
        const containers = document.querySelectorAll('.letter-pairs-container');
        
        containers.forEach(container => {
            const items = container.querySelectorAll('.letter-pair-item');
            if (items.length === 0) return;
            
            const containerHeight = container.clientHeight;
            const itemHeight = Math.floor(containerHeight / items.length) - 4; // Account for margins
            
            items.forEach(item => {
                item.style.height = itemHeight + 'px';
                
                // Adjust font size based on item height
                const content = item.querySelector('.pair-content');
                const fontSizePercent = Math.min(Math.max(itemHeight * 0.33, 8), 20);
                content.style.fontSize = fontSizePercent + 'px';
            });
        });
    }
    
    // Initial resize
    resizeTiles();
    
    // Resize on window resize
    window.addEventListener('resize', resizeTiles);
});
