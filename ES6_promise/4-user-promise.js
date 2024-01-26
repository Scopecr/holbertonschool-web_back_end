function signUpUser(firstname, lastName) {
  return Promise.resolve({
    firstName,
    lastname,
  });
}

export default signUpUser;
