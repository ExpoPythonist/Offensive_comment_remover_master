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

const SelectPlan = ({options, value, selectHandler}) => {
    const currentOption = options.filter((el) => (el.value == value))[0] || [];
    return (
        <div className="pt1">
            <div className="flex flex-column items-start justify-center">
                <div className="plan-select-label pv1 br2 pointer ttu">Select plan:</div>
            </div>
            <ReactResponsiveSelect
                caretIcon={caretIcon}
                name="plan"
                options={[currentOption, ...options.filter((el) => (el.value !== value))]}
                onChange={selectHandler}
                selectedValue={value}
            />
            <style global jsx>
                {`
                .plan-select-label {
                  font-family: 'Open Sans', sans-serif;
                  color: #382C58;
                  font-weight: 700;
                  font-size: 0.6rem;
                  padding-top:0.2rem;
                }
                .caret-icon {
                  position: absolute;
                  right: 1rem;
                  top: 1.25rem;
                  fill: #333;
                }
                .rrs {
                  position: relative;
                  box-sizing: border-box;
                }

                .rrs *,
                .rrs *:before,
                .rrs *:after {
                  box-sizing: border-box;
                }

                .rrs__button {
                  border-radius: 0.25rem;
                  border: solid 1px #EAD7FB;
                  color: #555;
                  position: relative;
                  cursor: pointer;
                  height: 44px;
                  line-height: 44px;
                  background: #fff;
                  border-radius: 2px;
                  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.2);
                  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
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
                  list-style: none;
                  padding: 0;
                  margin: 0;
                  background: #fff;
                  position: absolute;
                  z-index: 2;
                  border-top: 1px solid #eee;
                  border-radius: 0 0 2px 2px;
                  top: 44px;
                  width: 100%;
                  height: 0;
                  visibility: hidden;
                  overflow: hidden;
                  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.2);
                }

                .rrs--options-visible .rrs__options {
                  height: auto;
                  visibility: visible;
                  overflow: auto;
                  -webkit-overflow-scrolling: touch;
                  max-height: 230px;
                }

                .rrs__option {
                  border: solid 1px #EAD7FB;
                  cursor: pointer;
                  padding: 0.75rem 1rem;
                  margin: 0;
                  border-top: #eee 1px solid;
                  color: #aab7c4;
                  font-family: "Microsoft Sans Serif";
                  font-weight: 100;
                  opacity: 1;
                }

                .rrs__option * {
                  pointer-events: none;
                }

                .rrs__option:first-of-type {
                  border-top: 0;
                }

                .rrs__option:focus {
                  outline: 0;
                }

                .rrs__option:hover {
                  background: #f5f5f5;
                  color: #7049E2;
                }

                .rrs__option:active {
                  background: #e1f5fe;
                }

                .rrs__option.rrs__option--next-selection {
                  background: #f1f8fb;
                  color: #7049E2;
                }

                .rrs__option.rrs__option--selected {
                  color: #7049E2;
                }

                .rrs__option.rrs__option--disabled {
                  color: #999999;
                  background: #f5f5f5;
                  cursor: default;
                }

                .rrs__label {
                  padding: 0 2rem 0 1rem;
                  display: inline-flex;
                  width: 100%;
                  max-width: 100%;
                  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
                  font-size: 14px;
                  background: transparent;
                  border: 1px solid rgba(0, 0, 0, 0);
                  white-space: nowrap;
                  text-overflow: ellipsis;
                  overflow: hidden;
                  color: #aab7c4;
                  font-family: "Microsoft Sans Serif";
                  font-weight: 100;
                  opacity: 1;
                }

                .rrs--options-visible .rrs__label,
                .rrs__button:focus .rrs__label {
                  border-bottom: 1px solid #fff;
                  outline: 0;
                }

                .rrs--has-changed .rrs__label {
                  color: #0273b5;
                }
                `}
            </style>
        </div>
    )
}

SelectPlan.propTypes = {
    options: PropTypes.arrayOf(PropTypes.shape({
        text: PropTypes.string.isRequired,
        value: PropTypes.number.isRequired
    })).isRequired,
    value: PropTypes.number.isRequired,
    selectHandler: PropTypes.func.isRequired
}

export default SelectPlan;


// WEBPACK FOOTER //
// app/javascript/components/SelectPlan/index.js