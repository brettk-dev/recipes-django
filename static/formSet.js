
function addForm(formName) {
  const forms = document.querySelectorAll(`.${formName}_forms`)
  const lastForm = forms[forms.length - 1]
  const formRegex = new RegExp(`${formName}-[\\d]+-`, 'g')

  const newForm = lastForm.cloneNode(true)
  newForm.innerHTML = newForm.innerHTML.replace(formRegex, `${formName}-${forms.length}-`)

  lastForm.insertAdjacentElement('afterend', newForm)

  const formManager = document.querySelector(`#id_${formName}-TOTAL_FORMS`)
  formManager.setAttribute('value', `${forms.length + 1}`)
}
