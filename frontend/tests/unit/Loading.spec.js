import Loading from '@/components/Loading.vue'
import { shallowMount } from '@vue/test-utils'

describe('Loading.vue', () => {
  it('renders when loading prop is true', () => {
    const wrapper = shallowMount(Loading, {
      propsData: { loading: true }
    })
    expect(wrapper.contains('.loading-component')).toBe(true)
  })
  it('does not render when loading prop is false', () => {
    const wrapper = shallowMount(Loading, {
      propsData: { loading: false }
    })
    expect(wrapper.contains('.loading-component')).toBe(false)
  })
})
