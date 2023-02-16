function revealPair(pair_id) {
    let card = $(`#pair-${pair_id}`);
    if(card.hasClass('revealed')) {
        window.open(`/admin/core/pair/${pair_id}/change/`, '_blank')
    }
    else {
        card.removeClass('bg-dark text-white')
        card.addClass('bg-light text-black revealed')
    }
}
