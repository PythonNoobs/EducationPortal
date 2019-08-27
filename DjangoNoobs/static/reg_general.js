function addClass(element, class_name) {
  if (!element.classList.contains(class_name)) {
    element.classList.add(class_name);
  }
}