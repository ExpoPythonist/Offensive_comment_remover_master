import React from 'react';
import PropTypes from 'prop-types';
import ReactResponsiveSelect from 'react-responsive-select';

const caretIcon = (
  <svg style={{width: '0.7rem', height: '0.7rem'}} className="caret-icon" x="0px" y="0px" width="0.7rem" height="0.7rem" viewBox="0 -20 100 125">
    <g>
      <path
        style={{
          baselineShift: 'baseline',
          opacity: 1,
          color: '#7049E2',
          fill: '#7049E2',
          fillOpacity: 1,
          stroke: '#7049E2',
          strokeWidth:6,
          marker: 'none',
          visibility: 'visible',
          display: 'inline',
          overflow: 'visible',
          enableBackground: 'new 0 0 100 100'
        }}
        d="M50.1,63.5L10.8,24.2c-3.6-3.6-9.9-1.1-9.9,4.1v0c0,1.5,0.6,3,1.7,4.1l43.3,43.3c2.3,2.3,5.9,2.3,8.2,0l43.3-43.3  c1.1-1.1,1.7-2.6,1.7-4.1v0c0-5.2-6.2-7.7-9.9-4.1L50.1,63.5"
      />
    </g>
  </svg>
);

const Select = ({options, value, selectHandler}) => {
  const currentOption = options.filter((el) => (el.value === value))[0];
  return (
    <div>
      <ReactResponsiveSelect
        caretIcon={caretIcon}
        name="period"
        options={[currentOption, ...options.filter((el) => (el.value !== value))]}
        onChange={selectHandler}
        selectedValue={value}
      />
      <style global jsx>
        {`
          .rrs {
            position: relative;
            box-sizing: border-box;
            font-family:'Open Sans',sans-serif;
            color:#382C58;
          }
          .rrs--has-changed .rrs__label {
            color: #382C58;
          }

          .rrs *,
          .rrs *:before,
          .rrs *:after {
            box-sizing: border-box;
          }
          .rrs__options {
            border-radius: .5rem;
            font-size: 0.7rem;
            font-family: 'Open Sans', sans-serif;
          }
          .rrs__button {
            position: relative;
            cursor: pointer;
            padding:0.3rem 0.5rem;
            background: #fff;
            -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
            font-family: 'Open Sans', sans-serif;
            color: #382C58;
            font-weight: 700;
            font-size: 0.7rem;
          }

          .rrs__button--disabled {
            color: #999999;
            background: #f5f5f5;
            cursor: default;
          }

          .rrs__button:focus {
            outline: 0;
          }

          .rrs__button + .rrs__options {
            font-weight: 500;
            list-style: none;
            padding: 0;
            margin: 0;
            background: #fff;
            position: absolute;
            z-index: 2;
            top: 32px;
            right:5px;
            width: 8rem;
            height: 0;
            visibility: hidden;
            overflow: hidden;
            -webkit-box-shadow: 0px 3px 22px -5px rgba(36,0,35,0.15);
            -moz-box-shadow: 0px 3px 22px -5px rgba(36,0,35,0.15);
            box-shadow: 0px 3px 22px -5px rgba(36,0,35,0.15);
          }

          .rrs--options-visible .rrs__options {
            height: auto;
            visibility: visible;
            overflow: auto;
            -webkit-overflow-scrolling: touch;
            max-height: 230px;
          }

          .rrs__option {
            cursor: pointer;
            padding: 0.7rem;
            margin: 0;
          }

          .rrs__option * {
            pointer-events: none;
          }

          .rrs__option:first-of-type {
          }

          .rrs__option:focus {
            outline: 0;
          }

          .rrs__option:hover {
            background: #f5f5f5;
            color: #0273b5;
          }

          .rrs__option:active {
            background: #e1f5fe;
          }
          .rrs__option:hover {
            background: #f5f5f5;
            color: #382C58;
          }

          .rrs__option.rrs__option--next-selection {
            background: #FFFFFF;
            color: #382C58;
          }

          .rrs__option.rrs__option--selected {
            font-weight: 700;
            color: #382C58;
          }
          .rrs__option.rrs__option--selected:after {
            position:absolute;
            right:0.7rem;
            top: 0.6rem;
            color: #7049E2;
            font-size: 1rem;
            content: '✓';
          }

          .rrs__label {
            padding: 0;
            display: inline-flex;
            width: 100%;
            max-width: 100%;
            -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
            font-size: inherit;
            background: transparent;
            white-space: nowrap;
            text-overflow: ellipsis;
            overflow: hidden;
            display: -webkit-box;
            display: -ms-flexbox;
            display: flex;
            -webkit-box-direction: normal;
            -webkit-box-orient: horizontal;
            -ms-flex-direction: row;
            flex-direction: row;
            -webkit-box-align: center;
            -ms-flex-align: center;
            align-items: center;
          }
          .rrs__label__text {
            flex-grow:1;
            padding-right:10px;
          }

          .rrs--options-visible .rrs__button {
            outline: 0;
          }
          .caret-icon {
          //  position: absolute;
            right: 1rem;
            top: 1.25rem;
            fill: #333;
          }

          .rrs--options-visible .caret-icon {
            transform: rotate(180deg);
            transition: all .2s ease-in;
          }
          .rrs__button:focus {
            outline: 0;
          }
        `}
      </style>
    </div>
  )
}

Select.propTypes = {
  options: PropTypes.arrayOf(PropTypes.shape({
    text: PropTypes.string.isRequired,
    value: PropTypes.string.isRequired
  })).isRequired,
  value: PropTypes.string.isRequired,
  selectHandler: PropTypes.func.isRequired
}


export default Select;



// WEBPACK FOOTER //
// app/javascript/components/Select/index.js