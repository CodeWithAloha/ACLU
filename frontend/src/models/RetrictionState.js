export const RestrictionStateType = {
  Valid: 'VALID',
  Invalid: 'INVALID',
  Warning: 'WARNING'
}
export class RestrictionState {
  constructor (state, description) {
    this.state = state
    this.color = '#000000'

    switch (this.state) {
      default:
      case RestrictionStateType.Valid:
        this.color = '#2ecc40'
        break
      case RestrictionStateType.Invalid:
        this.color = '#ff4136'
        break
      case RestrictionStateType.Warning:
        this.color = 'YELLOW'
        break
    }
  }
}
