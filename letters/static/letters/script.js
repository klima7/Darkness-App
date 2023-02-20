function revealPair(pair_id) {
    let card = $(`#pair-${pair_id}`);
    card.removeClass('bg-dark text-white');
    card.addClass('bg-light text-black revealed');
}

function setSelects() {
    const urlParams = new URL(window.location.toLocaleString()).searchParams;

    let type = urlParams.get('type') ?? 'edge';
    let count = urlParams.get('count') ?? '36';

    $(`#select-type`).val(type).change();
    $(`#select-count`).val(count).change();
}

function generate() {
    let type = $(`#select-type`).val();
    let count = $(`#select-count`).val();
    const params = `?type=${type}&count=${count}`;

    const url = window.location.origin + window.location.pathname + params;
    console.log(url)
    window.location = url;
}

setSelects();
