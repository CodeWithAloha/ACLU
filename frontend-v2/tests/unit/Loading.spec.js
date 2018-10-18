import { shallowMount } from '@vue/test-utils'
import Loading from '@/components/Loading.vue'

describe('Loading.vue', () => {
  it('renders when loading prop is true', () => {
    const wrapper = shallowMount(Loading, {
      propsData: { loading: true }
    })
    expect(wrapper.contains('.loading-page')).toBe(true)
  })
  it('does not render when loading prop is false', () => {
    const wrapper = shallowMount(Loading, {
      propsData: { loading: false }
    })
    expect(wrapper.contains('.loading-page')).toBe(false)
  })
})
