document.addEventListener('DOMContentLoaded', function() {
    const letterItems = document.querySelectorAll('.letter-item');
    const pairModal = new bootstrap.Modal(document.getElementById('pairModal'));
    const closeButtons = document.querySelectorAll('[data-bs-dismiss="modal"]');
    let selectedLetters = {
        first: null,
        second: null
    };

    function updateSelectionState() {
        letterItems.forEach(item => {
            const group = item.closest('.letters-column').dataset.group;
            item.classList.remove('selected', 'disabled');
            
            if (group === 'first') {
                if (selectedLetters.first) {
                    if (item.dataset.letter === selectedLetters.first) {
                        item.classList.add('selected');
                    } else {
                        item.classList.add('disabled');
                    }
                }
            } else if (group === 'second') {
                if (selectedLetters.second) {
                    if (item.dataset.letter === selectedLetters.second) {
                        item.classList.add('selected');
                    } else {
                        item.classList.add('disabled');
                    }
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

    function showPairInfo(data) {
        const pairContent = document.getElementById('pairContent');
        const modalTitle = document.getElementById('pairModalLabel');
        let content = '';

        // Update modal title with the letter pair
        modalTitle.textContent = `Pair ${data.first.char.toUpperCase()}${data.second.char.toUpperCase()}`;

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
        pairModal.show();
    }

    // Add click handlers for close buttons
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            pairModal.hide();
        });
    });

    // Add keyboard handler for Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            pairModal.hide();
        }
    });

    letterItems.forEach(item => {
        item.addEventListener('click', function() {
            const group = this.closest('.letters-column').dataset.group;
            const letter = this.dataset.letter;

            if (this.classList.contains('disabled')) {
                return;
            }

            if (group === 'first') {
                selectedLetters.first = letter;
            } else {
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
