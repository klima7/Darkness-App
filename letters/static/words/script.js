function revealPair(pair_id) {
    let card = $(`#pair-${pair_id}`);
    card.removeClass('bg-dark text-white');
    card.addClass('bg-light text-black revealed');
}

function setSelects() {
    console.log("Setting selects");
    const urlParams = new URL(window.location.toLocaleString()).searchParams;

    let fromLetter = urlParams.get('from') ?? 'a';
    let toLetter = urlParams.get('to') ?? 'z';
    let count = urlParams.get('count') ?? '36';

    $(`#select-from`).val(fromLetter).change();
    $(`#select-to`).val(toLetter).change();
    $(`#select-count`).val(count).change();
}

function generate() {
    let letterFrom = $(`#select-from`).val();
    let letterTo = $(`#select-to`).val();
    let count = $(`#select-count`).val();
    const params = `?from=${letterFrom}&to=${letterTo}&count=${count}`;
    const url = window.location.origin + window.location.pathname + params;
    window.location = url;
}

setSelects();
