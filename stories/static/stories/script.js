function setSelects() {
    const urlParams = new URL(window.location.toLocaleString()).searchParams;

    let fromLetter = urlParams.get('from') ?? 'a';
    let toLetter = urlParams.get('to') ?? 'z';
    let length = urlParams.get('length') ?? '8';
    let reveal = urlParams.get('reveal') ?? '0';

    $(`#select-from`).val(fromLetter).change();
    $(`#select-to`).val(toLetter).change();
    $(`#select-length`).val(length).change();
    $(`#select-reveal`).val(reveal).change();
}

function generate() {
    let letterFrom = $(`#select-from`).val();
    let letterTo = $(`#select-to`).val();
    let length = $(`#select-length`).val();
    let reveal = $(`#select-reveal`).val();
    const params = `?from=${letterFrom}&to=${letterTo}&length=${length}&reveal=${reveal}`;
    const url = window.location.origin + window.location.pathname + params;
    window.location = url;
}

setSelects();
