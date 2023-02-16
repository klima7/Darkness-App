function revealPair(pair_id) {
    let card = $(`#pair-${pair_id}`);
    card.removeClass('bg-dark text-white');
    card.addClass('bg-light text-black revealed');
}

function openPair(pair_id) {
    window.open(`/admin/core/pair/${pair_id}/change/`, '_blank');
}

function setSelects() {
    console.log("Setting selects");
    const urlParams = new URL(window.location.toLocaleString()).searchParams;

    let fromLetter = urlParams.get('from') ?? 'a';
    let toLetter = urlParams.get('to') ?? 'z';

    $(`#select-from`).val(fromLetter).change();
    $(`#select-to`).val(toLetter).change();
}

function generate() {
    let letterFrom = $(`#select-from`).val();
    let letterTo = $(`#select-to`).val();
    const params = `?from=${letterFrom}&to=${letterTo}`;
    const url = window.location.origin + window.location.pathname + params;
    window.location = url;
}

setSelects();
