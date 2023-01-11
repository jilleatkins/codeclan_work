import styled from 'style-components';

const Button = styled.button`
  font-size: 11px;
  padding: 7px;
  margin: 0.5em;
  border: 2px solid #ced7e0;
`

const LaunchSelector = ({launchIncrease, launchDecrease}) => {

  return (
    <>
      <Button onClick={launchDecrease}>Previous Launch</Button>
      <Button onClick={launchIncrease}>Next Launch</Button>
    </>
  )

}

export default LaunchSelector;