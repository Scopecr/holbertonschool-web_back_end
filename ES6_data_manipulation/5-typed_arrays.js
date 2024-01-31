export function createInt8TypedArray(array) {
  if (position < 0 || position >= lenght) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(lenght);
  const view = new DataView(buffer, 0);
  view.setInt8(position, value);
  return view;
}
