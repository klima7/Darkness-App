document.addEventListener('DOMContentLoaded', function() {
    const letterItems = document.querySelectorAll('.letter-item');
    const modalElement = document.getElementById('pairModal');
    const pairModal = new bootstrap.Modal(modalElement);
    const closeButtons = document.querySelectorAll('[data-bs-dismiss="modal"]');
    const waitButton = document.getElementById('waitButton');
    let selectedLetters = {
        first: null,
        second: null
    };
    let autoCloseTimer = null;
    let progressInterval = null;
    let waitMode = false;

    function cleanupTimers() {
        if (autoCloseTimer) {
            clearTimeout(autoCloseTimer);
            autoCloseTimer = null;
        }
        if (progressInterval) {
            clearInterval(progressInterval);
            progressInterval = null;
        }
    }

    function updateSelectionState() {
        letterItems.forEach(item => {
            item.classList.remove('selected', 'disabled');
            
            if (selectedLetters.first) {
                if (item.dataset.letter === selectedLetters.first) {
                    item.classList.add('selected');
                }
            }
            
            if (selectedLetters.second) {
                if (item.dataset.letter === selectedLetters.second) {
                    item.classList.add('selected');
                }
            }
        });
    }

    function resetSelection() {
        selectedLetters = {
            first: null,
            second: null
        };
        updateSelectionState();
    }

    function closeModal() {
        pairModal.hide();
        cleanupTimers();
    }

    function showPairInfo(data) {
        const pairContent = document.getElementById('pairContent');
        const modalTitle = document.getElementById('pairModalLabel');
        const adminEditLink = document.getElementById('adminEditLink');
        const modalProgress = document.getElementById('modalProgress');
        const progressContainer = modalProgress.closest('.progress');
        let content = '';

        // Cleanup any existing timers
        cleanupTimers();
        
        // Reset wait mode
        waitMode = false;
        waitButton.style.display = 'inline-block';
        progressContainer.style.display = 'block';

        // Update modal title with the letter pair
        modalTitle.textContent = `Pair ${data.first.char.toUpperCase()}${data.second.char.toUpperCase()}`;

        // Update admin edit link if pair exists
        if (data.id) {
            adminEditLink.href = `/admin/core/pair/${data.id}/change/`;
            adminEditLink.style.display = 'inline-block';
        } else {
            adminEditLink.style.display = 'none';
        }

        if (data.error) {
            content = `<div class="alert alert-danger">${data.error}</div>`;
        } else {
            content = `
                <div class="mb-4 text-center">
                    <h6 class="text-muted mb-2">Best Word</h6>
                    <div class="best-word" style="font-size: 3rem; font-weight: bold;">
                        ${data.best_word?.word || 'No best word set'}
                    </div>
                    ${data.best_word?.description ? `
                        <div class="mt-2" style="font-size: 1.2rem;">
                            ${data.best_word.description}
                        </div>
                    ` : ''}
                </div>
                <div class="mt-4">
                    <h6>All Words:</h6>
                    <ul class="list-unstyled">
                        ${data.words.map(word => `
                            <li class="mb-2">
                                <strong>${word.word}</strong>
                                ${word.description ? `<span class="text-muted"> - ${word.description}</span>` : ''}
                            </li>
                        `).join('')}
                    </ul>
                </div>
            `;
        }

        pairContent.innerHTML = content;
        
        // Reset progress bar
        modalProgress.style.width = '100%';
        
        // Show modal
        pairModal.show();
        
        // Only start progress bar and auto-close timer if not in wait mode
        if (!waitMode) {
            // Start progress bar animation
            const duration = 5000; // 5 seconds
            const steps = 100;
            const stepTime = duration / steps;
            let currentStep = 0;
            
            progressInterval = setInterval(() => {
                currentStep++;
                const progress = 100 - (currentStep / steps * 100);
                modalProgress.style.width = `${progress}%`;
                
                if (currentStep >= steps) {
                    clearInterval(progressInterval);
                    progressInterval = null;
                }
            }, stepTime);
    
            // Start auto-close timer
            autoCloseTimer = setTimeout(() => {
                closeModal();
            }, duration);
        }
    }

    // Add wait button handler
    waitButton.addEventListener('click', function() {
        // Hide the wait button
        this.style.display = 'none';
        
        // Enable wait mode
        waitMode = true;
        cleanupTimers();
        
        // Hide progress bar
        const progressContainer = document.querySelector('.progress');
        progressContainer.style.display = 'none';
    });

    // Add click handlers for close buttons
    closeButtons.forEach(button => {
        button.addEventListener('click', closeModal);
    });

    // Add keyboard handler for Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && modalElement.classList.contains('show')) {
            closeModal();
        }
    });

    // Add modal hidden event handler
    modalElement.addEventListener('hidden.bs.modal', cleanupTimers);

    letterItems.forEach(item => {
        item.addEventListener('click', function() {
            const letter = this.dataset.letter;

            if (!selectedLetters.first) {
                selectedLetters.first = letter;
            } else if (!selectedLetters.second) {
                selectedLetters.second = letter;
            }

            updateSelectionState();

            if (selectedLetters.first && selectedLetters.second) {
                // Make API call
                fetch(`/search/api/pair/?letter1=${selectedLetters.first.toLowerCase()}&letter2=${selectedLetters.second.toLowerCase()}`)
                    .then(response => response.json())
                    .then(data => {
                        showPairInfo(data);
                        resetSelection();
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        showPairInfo({ error: 'Failed to fetch pair information' });
                        resetSelection();
                    });
            }
        });
    });
});
