function openPair(pair_id, blank) {
  if(blank === true) {
    window.open(`/admin/core/pair/${pair_id}/change/`, '_blank');
  }
  else {
    window.location = `/admin/core/pair/${pair_id}/change/`;
  }
}
