from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_schedule_summaries_locale import GetScheduleSummariesLocale
from ...models.get_schedule_summaries_response_200 import GetScheduleSummariesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    locale: GetScheduleSummariesLocale,
    urn_date: str,
    *,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = UNSET,
    format: str = "json",  # Added format parameter with default "json"
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/schedules/{urn_date}/summaries" + f".{format}",  # Append format to URL
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetScheduleSummariesResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetScheduleSummariesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetScheduleSummariesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    locale: GetScheduleSummariesLocale,
    urn_date: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = UNSET,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetScheduleSummariesResponse200]:
    """get a list of summaries for all sport events in a day (any status)

     Get a list of summaries for all sport events in a day (any status).

    Args:
        locale (GetScheduleSummariesLocale):
        urn_date (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetScheduleSummariesResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_date=urn_date, offset=offset, limit=limit, format=format)

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    locale: GetScheduleSummariesLocale,
    urn_date: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = UNSET,
    format: str = "json",  # Added format parameter to shorthand function as well
) -> Optional[GetScheduleSummariesResponse200]:
    """get a list of summaries for all sport events in a day (any status)

     Get a list of summaries for all sport events in a day (any status).

    Args:
        locale (GetScheduleSummariesLocale):
        urn_date (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetScheduleSummariesResponse200
    """

    return sync_detailed(
        locale=locale,
        urn_date=urn_date,
        client=client,
        offset=offset,
        limit=limit,
        format=format,  # Pass format to sync_detailed
    ).parsed


async def asyncio_detailed(
    locale: GetScheduleSummariesLocale,
    urn_date: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = UNSET,
    format: str = "json",  # Added format parameter with default "json"
) -> Response[GetScheduleSummariesResponse200]:
    """get a list of summaries for all sport events in a day (any status)

     Get a list of summaries for all sport events in a day (any status).

    Args:
        locale (GetScheduleSummariesLocale):
        urn_date (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetScheduleSummariesResponse200]
    """

    kwargs = _get_kwargs(locale=locale, urn_date=urn_date, offset=offset, limit=limit, format=format)

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    locale: GetScheduleSummariesLocale,
    urn_date: str,
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = UNSET,
    format: str = "json",  # Added format parameter to async shorthand function
) -> Optional[GetScheduleSummariesResponse200]:
    """get a list of summaries for all sport events in a day (any status)

     Get a list of summaries for all sport events in a day (any status).

    Args:
        locale (GetScheduleSummariesLocale):
        urn_date (str):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetScheduleSummariesResponse200
    """

    return (
        await asyncio_detailed(
            locale=locale,
            urn_date=urn_date,
            client=client,
            offset=offset,
            limit=limit,
            format=format,  # Pass format to asyncio_detailed
        )
    ).parsed
